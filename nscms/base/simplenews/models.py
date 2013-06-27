#-*- coding:utf-8 -*-

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db import models

from nscms.base.content.models import ContentModel


SIMPLENEWS_IMAGE_UPLOAD_TO = \
    getattr(settings, "SIMPLENEWS_IMAGE_UPLOAD_TO", "simplenews")


class SimpleNewsModel(ContentModel):
    image = models.ImageField(
        upload_to=SIMPLENEWS_IMAGE_UPLOAD_TO, max_length=255, blank=True)

    class Meta:
        ordering = ['-publish_date']
        verbose_name = _(u"Notícia")
        verbose_name_plural = _(u"Notícias")
        abstract = True
