django-wiki
===========

Super simple pluggable wiki application for Django.

Authors
-------
John Sutherland (https://github.com/sneeu)

Taylor Mitchell (https://github.com/tmitchell)

Sebastián Magrí (https://github.com/sebasmagri)

Basic Usage
-----------

For the default URL setup, add the following line to your root
URLConf::

   (r'^wiki/', include('wiki.urls')),

This will set up the following URL patterns:

* ``/wiki`` will be the view to list all of the wiki pages.

* ``/wiki/<name>/`` will be the view for the latest revision of
  a wiki page.  It has a url name of ``wiki-view-page``.

* ``/wiki/<name>/<rev>`` will be the view for a specific revision
  of a wiki page.  It has a url name of ``wiki-view-revision``.

* ``/wiki/<name>/diff/<rev>`` will be the view for the diffs for
  a specific revision of a wiki page.  It has a url name of ``wiki-view-diff``.

* ``/wiki/<name>/edit`` will be the view to edit a wiki page.  It has a
  url name of ``wiki-edit-page``.

The default wiki page name format is `WikiWord`_.  You can customize the naming
convention if desired by adding your own regular expression to your settings.py
like this::

    WIKI_WORD = r'(?:[A-Z]+[a-z]+){2,}'

Dependencies
------------

``Django>=1.2.5``

``Markdown``

Bug Reports/Feature Requests
----------------------------

Pop over to this app's `project page on Github`_ and
check `the issues list`_ to see if it's already been reported. If not,
open a new issue and I'll do my best to respond quickly.

.. _WikiWord: http://twiki.org/cgi-bin/view/TWiki/WikiWord
.. _project page on Github: https://github.com/sebasmagri/django-wiki
.. _the issues list: https://github.com/sebasmagri/django-wiki/issues
