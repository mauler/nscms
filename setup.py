#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cemese",
    version = "0.0.1",
    author = "Paulo Roberto Macedo",
    author_email = "proberto.macedo@gmail.com",
    description = ("A package of tools to create a lazy cms on pt_BR language "
                   "(without i18n)."),
    license = "BSD",
    keywords = "cms content",
    url = "hhttps://github.com/mauler/django-cemese",
    packages=['cemese', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
    ],
)

