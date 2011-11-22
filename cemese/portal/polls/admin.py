#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    inlines = (ChoiceInline, )
    search_fields = ("title", "description", "choice__title", )

admin.site.register(Question, QuestionAdmin)

