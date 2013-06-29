#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.db import models

from nscms.base.content.models import ContentModel


class News(ContentModel):
    body = models.TextField()

    class Meta(ContentModel.Meta):
        abstract = False
        verbose_name = u"Notícia"
        verbose_name_plural = u"Notícias"
