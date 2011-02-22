from django.conf.urls.defaults import *

from templatetags.wiki import WIKI_WORD

urlpatterns = patterns(
    'wiki.views',
    url(r'^$', 'index', name = 'wiki-index'),
    # url(r'^$', 'main', name='wiki-main-page'),
    # url(r'^index/$', 'index', name = 'wiki-index'), # ?by={name,date}
    url('^(?P<name>%s)/$' % WIKI_WORD, 'view', name = 'wiki-view-page'),
    url('^(?P<name>%s)/(?P<rev>\d+)/$' % WIKI_WORD,
        'view',
        name = 'wiki-view-revision'),
    url('^(?P<name>%s)/diff/(?P<rev>\d+)/$' % WIKI_WORD,
        'view_diff',
        name = 'wiki-view-diff'),
    url('^(?P<name>%s)/edit/$' % WIKI_WORD,
        'edit',
        name = 'wiki-edit-page'),
    url('^(?P<name>%s)/delete/$' % WIKI_WORD,
        'delete',
        name = 'wiki-delete-page'),
)
