from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from forms import PageForm
from models import Page, Revision

def index(request):
    """Lists all pages stored in the wiki."""
    pages = Page.objects.all()

    ctx = {'pages': pages}
    return render_to_response('wiki/index.html', ctx, context_instance=RequestContext(request))

def view_diff(request, name, rev=None):
    """Shows the diffs for a wiki revision"""
    try:
        page = Page.objects.get(name=name)
        if rev is not None:
            rev = int(rev)
            revision = get_object_or_404(Revision, page=page, counter=rev)
        else:
            revision = page.get_latest_revision()
    except Page.DoesNotExist:
        page = Page(name=name)
        revision = None

    # compute diff
    import difflib
    prev_content = ""
    if revision and revision.get_prev():
        prev_content = revision.get_prev().content

    #diff = difflib.HtmlDiff().make_table(revision.content.splitlines(), prev_content.splitlines())
    d = difflib.Differ()
    diff = d.compare(prev_content.splitlines(), revision.content.splitlines())
    diff = '\n'.join(list(diff))

    ctx = { 'page': page, 'revision': revision, 'diff': diff }
    return render_to_response('wiki/diff.html', ctx, context_instance=RequestContext(request))

def view(request, name, rev=None):
    """Shows a single wiki page."""
    try:
        page = Page.objects.get(name=name)
        if rev is not None:
            rev = int(rev)
            revision = get_object_or_404(Revision, page=page, counter=rev)
        else:
            revision = page.get_latest_revision()
    except Page.DoesNotExist:
        page = Page(name=name)
        revision = None

    ctx = { 'page': page, 'revision': revision }
    return render_to_response('wiki/view.html', ctx, context_instance=RequestContext(request))


def edit(request, name):
    """Allows users to edit wiki pages."""
    try:
        page = Page.objects.get(name=name)
    except Page.DoesNotExist:
        page = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if not page:
                page = Page()
            page.name = form.cleaned_data['name']
            page.save()

            revision = Revision()
            revision.page = page
            revision.content = form.cleaned_data['content']
            if request.user.is_authenticated():
                revision.editor = request.user
            revision.save()
            return HttpResponseRedirect(page.get_absolute_url())
    else:
        if page:
            revision = page.get_latest_revision()
            form = PageForm(initial={'name': page.name, 'content': revision.content})
        else:
            form = PageForm(initial={'name': name})

    ctx = { 'form': form }
    return render_to_response('wiki/edit.html', ctx, context_instance=RequestContext(request))
