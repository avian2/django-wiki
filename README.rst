django-wiki
===========

Super simple pluggable wiki application for Django.

Authors
-------
John Sutherland (https://github.com/sneeu)

Taylor Mitchell (https://github.com/tmitchell)

Sebastián Magrí (https://github.com/sebasmagri)

Dependencies
------------

``Django>=1.2.5``

``Markdown``

``django-staticfiles`` (will be included in Django-1.3 as ``django.contrib.staticfiles``)

You can install all required modules using `pip`_::

    pip install -r requirements.txt

Basic Usage
-----------

Add ``staticfiles`` (``django.contrib.staticfiles`` if you're using
``Django>=1.3``) and ``wiki`` to the ``INSTALLED_APPS`` tuple in your
project's ``settings.py``.

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

Add the ``staticfiles.context_processors.static`` context processor to your 
``TEMPLATE_CONTEXT_PROCESSORS``. If you're using ``Django<=1.3`` please read
the official `staticfiles tutorial`_ on that `topic`_.

Bug Reports/Feature Requests
----------------------------

Pop over to this app's `project page`_ on `Github`_ and
check the `issues`_ list to see if it's already been reported. If not,
open a new issue and I'll do my best to respond quickly.

.. _pip: http://pip.openplans.org/
.. _WikiWord: http://twiki.org/cgi-bin/view/TWiki/WikiWord
.. _Github: https://github.com/
.. _project page: https://github.com/sebasmagri/django-wiki/
.. _issues: https://github.com/sebasmagri/django-wiki/issues/
.. _staticfiles tutorial: http://docs.djangoproject.com/en/dev/howto/static-files/
.. _topic: http://docs.djangoproject.com/en/dev/howto/static-files/#with-a-context-processor
