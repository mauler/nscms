#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    fields = ("title", "body", ("published", "publish_date", ))


admin.site.register(News, NewsAdmin)
