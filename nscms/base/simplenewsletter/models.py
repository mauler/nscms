#-*- coding:utf-8 -*-

from nscms.base.content.models import CreationModificationModel

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import UUIDField


class SimpleNewsletterModel(CreationModificationModel):
    email = models.EmailField(unique=True)
    uuid = UUIDField()

    class Meta:
        abstract = True
        verbose_name = _(u"Inscrição")
        verbose_name_plural = _(u"Inscrições")

    def __unicode__(self):
        return self.email
