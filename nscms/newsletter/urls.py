#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^inscrever$', 'cemese.newsletter.views.inscrever', name='inscrever'),
    url(r'^remover$', 'cemese.newsletter.views.remover', name='remover'),
)

