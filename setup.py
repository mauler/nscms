#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup
import os


README = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()


CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',  # example license
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks'
]

setup(
    name="nscms",
    version="0.0.1",
    description=u"A CMS core to build portals.",
    long_description=README,
    author="Paulo Roberto",
    author_email="proberto.macedo@gmail.com",
    url="http://github.com/mauler/django-cemese",
    license="BSD License",
    platforms=['OS Independent'],
    packages=['nscms'],
    include_package_data=True,
    classifiers=CLASSIFIERS,
)
