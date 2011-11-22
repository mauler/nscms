#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.http import HttpResponse

from models import Inscricao


def inscrever(request):
    if 'email' in request.GET:
        Inscricao.objects.get_or_create(email=request.GET['email'])
        return HttpResponse(mimetype="text/json")

