#-*- coding:utf-8 -*-

from django.contrib import admin
from django.db import models


class Subscription(models.Model):
    email = models.EmailField()

    class Admin(admin.ModelAdmin):
        pass

    class Meta:
        verbose_name = u"Inscrição"
        verbose_name_plural = u"Inscrições"

    def __unicode__(self):
        return self.email
