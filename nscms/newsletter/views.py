#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import redirect

from models import Subscription


def register(request):
    if 'email' in request.GET:
        Subscription.objects.get_or_create(email=request.GET['email'])
        return HttpResponse(mimetype="text/json")


def remove(request):
    Subscription.objects.get(
        pk=request.GET['pk'], email=request.GET['email']).delete()
    return redirect(request.GET['redirect_to'])
