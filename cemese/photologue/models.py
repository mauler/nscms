#!/usr/bin/env python
#-*- coding:utf-8 -*-

from cStringIO import StringIO
import os
import zipfile

from PIL import Image

from django.conf import settings
from django.core.files.base import ContentFile
from django.db import models

from photologue.models import ImageModel


class PhotoSizeEmulator(object):
    photosize_attr = 'image'

    def admin_thumbnail(self):
        im = ImageModel()
        im.image = getattr(self, self.get_photosize_attr())
        if im.image:
            return im.admin_thumbnail()
        else:
            return ''
    admin_thumbnail.allow_tags = True
    admin_thumbnail.short_description = "Thumbnail"

    def __getattr__(self, name, *args, **kwargs):
        if name != 'get_absolute_url' and \
           name.startswith("get_") and \
           name.endswith("_url"):
            im = ImageModel()
            attr = self.get_photosize_attr()
            if isinstance(attr, str):
                im.image = getattr(self, attr)
            else:
                im.image = attr
            if im.image:
                func = getattr(im, name)
                return func
        return super(PhotoSizeEmulator, self).__getattr__(name, *args, **kwargs)

    def get_photosize_attr(self):
        return self.photosize_attr

    def get_photosize_url(self, photosize_name):
        im = ImageModel()
        im.image = getattr(self, self.get_photosize_attr())
        return getattr(im, "get_%s_url" % photosize_name)()

class GalleryUploadEmulator(models.Model):
    zip_file = models.FileField("arquivo de imagens (.zip)",
                                upload_to="galeria-zip",
                                help_text=u"O arquivo enviado sera processado e removido, as fotos ficarão disponíveis na galeria.",
                                blank=True)
    zip_title = models.CharField(u"Título padrão", blank=True, max_length=100)
    zip_credits = models.CharField(u"Créditos padrão", blank=True, max_length=100)

    class Meta:
        abstract = True

    def galleryupload_save(self, *args, **kwargs):
        if self.zip_file:
            self.process_zipfile()
            self.zip_file.delete()
            self.zip_file = ''
            self.save(*args, **kwargs)

    def process_zipfile(self):
        if os.path.isfile(self.zip_file.path):
            qset = self.get_zipfile_qset()
            # TODO: implement try-except here
            zip = zipfile.ZipFile(self.zip_file.path)
            bad_file = zip.testzip()
            if bad_file:
                raise Exception('"%s" in the .zip archive is corrupt.' % bad_file)
            count = 1

            for filename in sorted(zip.namelist()):
                if filename.startswith('__'): # do not process meta files
                    continue
                data = zip.read(filename)
                if len(data):
                    try:
                        # the following is taken from django.newforms.fields.ImageField:
                        #  load() is the only method that can spot a truncated JPEG,
                        #  but it cannot be called sanely after verify()
                        trial_image = Image.open(StringIO(data))
                        trial_image.load()
                        # verify() is the only method that can spot a corrupt PNG,
                        #  but it must be called immediately after the constructor
                        trial_image = Image.open(StringIO(data))
                        trial_image.verify()
                    except Exception:
                        # if a "bad" file is found we just skip it.
                        continue
                    while 1:
                        title = ' '.join([self.title, str(count)])
                        img = qset.create(title=self.zip_title or title,
                                          creditos=self.zip_credits or "upload")
                        img.image.save(filename, ContentFile(data))
                        count+= 1
                        break
            zip.close()
            return self

