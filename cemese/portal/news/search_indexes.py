#!/usr/bin/env python
#-*- coding:utf-8 -*-

from haystack.indexes import *
from haystack import site

from models import News

class NewsIndex(RealTimeSearchIndex):
    title = CharField(model_attr="title")
    description = CharField(model_attr="description")
    body = CharField(document=True, model_attr="body")

    def index_queryset(self):
        return News.objects.published()

site.register(News, NewsIndex)

