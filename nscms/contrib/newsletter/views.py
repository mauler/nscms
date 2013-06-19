 #!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.http import HttpResponse

from .models import Subscription


def optin(request):
    if 'email' in request.GET:
        Subscription.objects.get_or_create(email=request.GET['email'])
    return HttpResponse()
