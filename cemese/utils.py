#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

from django.template.defaultfilters import slugify


def slugify_filename(filename):
    name, ext = os.path.splitext(filename)
    return slugify(name) + ext

