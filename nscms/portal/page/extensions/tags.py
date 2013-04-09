#-*- coding:utf-8 -*-

from taggit.managers import TaggableManager


def register(cls, admin_cls):
    cls.add_to_class('tags', TaggableManager(blank=True))
    admin_cls.fieldsets[0][1]['fields'].append("tags")
