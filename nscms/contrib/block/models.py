#-*- coding:utf-8 -*-

from nscms.base.content.models import SimpleContentModel, \
    PublisherModel

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField


class Block(SimpleContentModel, PublisherModel):
    content = RichTextField(verbose_name=_(u"Content"))

    class Meta:
        verbose_name = _(u"Block")
        verbose_name_plural = _(u"Block")
