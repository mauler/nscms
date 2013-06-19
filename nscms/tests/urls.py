#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^newsletter/',
        include('nscms.contrib.newsletter.urls', namespace="newsletter")),
)
