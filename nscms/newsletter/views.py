#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import redirect

from models import Inscricao


def inscrever(request):
    if 'email' in request.GET:
        Inscricao.objects.get_or_create(email=request.GET['email'])
        return HttpResponse(mimetype="text/json")


def remover(request):
    Inscricao.objects.get(pk=request.GET['pk'], email=request.GET['email']).delete()
    return redirect(request.GET['redirect_to'])

