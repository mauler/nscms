#-*- coding:utf-8 -*-

from django.contrib import admin

from models import News


admin.site.register(News, News.Admin)
