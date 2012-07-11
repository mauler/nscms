#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup
import os

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name="django-cemese",
    version="0.0.1",
    author="Paulo Roberto Macedo Chaves",
    author_email="proberto.macedo@gmail.com",
    description="A package with a lot of tools to that helps my self to " \
                "create cms projects using Django.",
    license="BSD",
    keywords="cms content blog",
    url="http://github.com/mauler/django-cemese",
    packages=["cemese"],
    long_description=read('README.md'),
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django',
        'django-ckeditor',
#        'FeinCMS',
#        'django-mptt',
#        'django-taggit',
        'django-extensions'
    ],
)

