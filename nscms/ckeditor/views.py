#-*- coding:utf-8 -*-

import os
from datetime import datetime

from django.conf import settings
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from cemese.utils import slugify_filename


try:
    from PIL import Image, ImageOps
except ImportError:
    import Image, ImageOps

try:
    from django.views.decorators.csrf import csrf_exempt
except ImportError:
    # monkey patch this with a dummy decorator which just returns the same function
    # (for compatability with pre-1.1 Djangos)
    def csrf_exempt(fn):
        return fn

from ckeditor.views import *


@csrf_exempt
def upload(request):
    """
    Uploads a file and send back its URL to CKEditor.

    TODO:
        Validate uploads
    """
    # Get the uploaded file from request.
    upload = request.FILES['upload']
    upload_ext = os.path.splitext(upload.name)[1]

    if getattr(settings, 'CKEDITOR_RESTRICT_BY_USER', False):
        user_path = user.username
    else:
        user_path = ''
    date_path = datetime.now().strftime('%Y/%m/%d')
    upload_path = os.path.join(
        settings.CKEDITOR_UPLOAD_PATH, user_path, date_path)
    path = os.path.join(upload_path, slugify_filename(upload.name))
    default_storage.save(path, upload)
    upload_filename = path

#    # Open output file in which to store upload.
#    upload_filename = get_upload_filename(upload.name, request.user)
#    out = open(upload_filename, 'wb+')

#    # Iterate through chunks and write to destination.
#    for chunk in upload.chunks():
#        out.write(chunk)
#    out.close()

    try:
        create_thumbnail(upload_filename)
    except:
        pass

    # Respond with Javascript sending ckeditor upload url.
    url = get_media_url(upload_filename)
    return HttpResponse("""
    <script type='text/javascript'>
        window.parent.CKEDITOR.tools.callFunction(%s, '%s');
    </script>""" % (request.GET['CKEditorFuncNum'], url))
