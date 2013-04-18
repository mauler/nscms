#-*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.db import models

from nscms.base.db.models import PublisherModel, ContentModel


class SimpleNewsModel(ContentModel, PublisherModel):
    image = models.ImageField(upload_to='/simplesnews/', max_length=255)

    class Meta:
        ordering = ['-publish_date']
        verbose_name = _(u"Notícia")
        verbose_name_plural = _(u"Notícias")
        abstract = True
