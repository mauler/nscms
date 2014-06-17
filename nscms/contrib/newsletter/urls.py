# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'nscms.contrib.newsletter.views',
    url(
        r'^optin/$',
        'optin',
        name="optin"
    ),
)
