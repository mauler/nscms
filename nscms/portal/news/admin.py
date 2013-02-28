#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from models import News


admin.site.register(News, News.Admin)

