#!/usr/bin/env python
#-*- coding:utf-8 -*-

from uuid import uuid4

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import models


class UserProfileModel(models.Model):
    user = models.OneToOneField("auth.User")

    class Meta:
        abstract = True

    def auth_login(self, request,
            backend='django.contrib.auth.backends.ModelBackend'):
        self.user.backend = backend
        login(request, self.user)

    def save(self, *args, **kwargs):
        try:
            self.user
        except User.DoesNotExist:
            username = u"%s" % uuid4()
            username = username[:30]
            self.user = user = User.objects.create(username=username)
            user_set_password = getattr(self, '_user_set_password', None)
            if user_set_password is not None:
                user.set_password(user_set_password)
                user.save()
            usercreated = True
        else:
            usercreated = False
        saved = super(UserProfileModel, self).save(*args, **kwargs)
        if usercreated:
            user.username = \
                u'%s-%d' % (self.__class__.__name__.lower(), self.id)
            user.save()

        return saved
