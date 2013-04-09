#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.contrib.admin import site

from models import Inscricao


site.register(Inscricao, Inscricao.Admin)
