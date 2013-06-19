#-*- coding:utf-8 -*-

from nscms.base.content.models import CreationModificationModel

from django.utils.translation import ugettext_lazy as _
from django.db import models

from django_extensions.db.fields import UUIDField


class Subscription(CreationModificationModel):

    email = models.EmailField(unique=True)
    uuid = UUIDField()

    class Meta:
        verbose_name = _(u"Inscrição")
        verbose_name_plural = _(u"Inscrições")
        ordering = ("-created", )

    def __unicode__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super(Subscription, self).save(*args, **kwargs)
