from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from forms import PageForm
from models import Page, Revision

@login_required
def index(request, template_name = 'wiki/index.html'):
    '''
    Lists all pages stored in the wiki
    '''
    pages = Page.objects.all()

    context = {
        'pages' : pages
        }
    return render_to_response(
        template_name,
        context,
        context_instance = RequestContext(request)
        )

@login_required
def view_diff(request, name, rev = None, template_name = 'wiki/diff.html'):
    '''
    Shows the diffs for a wiki revision
    '''
    try:
        page = Page.objects.get(name = name)
        if rev is not None:
            rev = int(rev)
            revision = get_object_or_404(Revision, page = page, counter = rev)
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

    d = difflib.Differ()
    diff = d.compare(prev_content.splitlines(), revision.content.splitlines())
    diff = '\n'.join(list(diff))

    context = {
        'page' : page,
        'revision' : revision,
        'diff' : diff
        }
    return render_to_response(
        template_name,
        context,
        context_instance = RequestContext(request)
        )

@login_required
def view(request, name, rev = None, template_name = 'wiki/view.html'):
    '''
    Shows a single wiki page
    '''
    try:
        page = Page.objects.get(name = name)
        if rev is not None:
            rev = int(rev)
            revision = get_object_or_404(Revision, page = page, counter = rev)
        else:
            revision = page.get_latest_revision()
    except Page.DoesNotExist:
        page = Page(name=name)
        revision = None

    context = {
        'page' : page,
        'revision' : revision
        }
    return render_to_response(
        template_name,
        context,
        context_instance = RequestContext(request)
        )


@login_required
def edit(request, name, template_name = 'wiki/edit.html'):
    '''
    Allows users to edit wiki pages
    '''
    try:
        page = Page.objects.get(name = name)
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
            return redirect(page)
    else:
        if page:
            revision = page.get_latest_revision()
            form = PageForm(
                initial = {
                    'name' : page.name,
                    'content' : revision.content
                    }
                )
        else:
            form = PageForm(
                initial = {
                    'name' : name,
                    }
                )

    context = {
        'form' : form,
        }
    return render_to_response(
        template_name,
        context,
        context_instance = RequestContext(request)
        )

@login_required
def delete(request, name, template_name = 'wiki/confirm_delete.html'):
    if request.method == 'POST':
        page = Page.objects.get(name = name)
        page.delete()
        return redirect('wiki-index')
    else:
        return render_to_response(
            template_name,
            {
                'page_name' : name,
                },
            context_instance = RequestContext(request)
            )
