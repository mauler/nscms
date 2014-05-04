#-*- coding:utf-8 -*-

from nscms.base.content.models import SimpleContentModel, \
    PublisherModel

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Block(SimpleContentModel, PublisherModel):
    content = models.TextField(verbose_name=_(u"Content"))
    is_template = models.BooleanField(
        default=False,
        help_text=_(
            u"Check this if the block is a Django Template and needs "
            u"to be processed."),
        verbose_name=_(u"Is a template ?"),
    )

    class Meta:
        verbose_name = _(u"Block")
        verbose_name_plural = _(u"Block")
