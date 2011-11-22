#!/usr/bin/env python
#-*- coding:utf-8 -*-

# COPY AND PASTE !!!

"""
Views and functions for serving static files. These are only to be used
during development, and SHOULD NOT be used in a production setting.
"""

import mimetypes
import os
import posixpath
import re
import urllib

from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotModified
from django.shortcuts import render
from django.template import loader, Template, Context, TemplateDoesNotExist, RequestContext
from django.utils.http import http_date, parse_http_date
from django.views.static import *

def templateserve(request, path, document_root=None, show_indexes=False,
                  extra_context={}):
    """
    Serve static files below a given point in the directory structure.

    To use, put a URL pattern such as::

        (r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root' : '/path/to/my/files/'})

    in your URLconf. You must provide the ``document_root`` param. You may
    also set ``show_indexes`` to ``True`` if you'd like to serve a basic index
    of the directory.  This index view will use the template hardcoded below,
    but if you'd like to override it, you can create a template called
    ``static/directory_index.html``.
    """
    path = posixpath.normpath(urllib.unquote(path))
    path = path.lstrip('/')
    newpath = ''
    for part in path.split('/'):
        if not part:
            # Strip empty path components.
            continue
        drive, part = os.path.splitdrive(part)
        head, part = os.path.split(part)
        if part in (os.curdir, os.pardir):
            # Strip '.' and '..' in path.
            continue
        newpath = os.path.join(newpath, part).replace('\\', '/')
    if newpath and path != newpath:
        return HttpResponseRedirect(newpath)
    fullpath = os.path.join(document_root, newpath)
    if os.path.isdir(fullpath):
        index = os.path.join(fullpath, "index.html")
        if os.path.exists(index):
                fullpath = index
        elif show_indexes:
            return directory_index(newpath, fullpath)
        else:
            raise Http404("Directory indexes are not allowed here.")
    if not os.path.exists(fullpath):
        fullpath+= '.html'
        if not os.path.exists(fullpath):
            raise Http404('"%s" does not exist' % fullpath)
    # Respect the If-Modified-Since header.
    statobj = os.stat(fullpath)
    mimetype, encoding = mimetypes.guess_type(fullpath)
    mimetype = mimetype or 'application/octet-stream'
    if not was_modified_since(request.META.get('HTTP_IF_MODIFIED_SINCE'),
                              statobj.st_mtime, statobj.st_size):
        return HttpResponseNotModified(mimetype=mimetype)
    if fullpath.endswith(".html") or fullpath.endswith(".php"):
        return render(request, fullpath, extra_context)
    response = HttpResponse(open(fullpath, 'rb').read(), mimetype=mimetype)
    response["Last-Modified"] = http_date(statobj.st_mtime)
    response["Content-Length"] = statobj.st_size
    if encoding:
        response["Content-Encoding"] = encoding
    return response

