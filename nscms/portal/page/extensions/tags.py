#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.db import models
from taggit.managers import TaggableManager
from taggit.models import Tag
def register(cls, admin_cls):
#    cls.add_to_class("tags", models.ManyToManyField("taggit.Tag", blank=True))
    cls.add_to_class('tags', TaggableManager(blank=True))
    admin_cls.fieldsets[0][1]['fields'].append("tags")

