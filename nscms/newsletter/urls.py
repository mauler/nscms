#-*- coding:utf-8 -*-

from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^inscrever$', 'nscms.newsletter.views.inscrever', name='inscrever'),
    url(r'^remover$', 'nscms.newsletter.views.remover', name='remover'),
)
