#-*- coding:utf-8 -*-

from nscms.base.content.models import SimpleContentModel, \
    PublisherModel

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField


class SimplePageModel(MPTTModel, SimpleContentModel, PublisherModel):
    parent = TreeForeignKey(
        'self', verbose_name=_(u"Pai"), null=True, blank=True,
        related_name='children')
    content = RichTextField(verbose_name=_(u"Conteúdo"))
    redirect_to = TreeForeignKey(
        'self', verbose_name=_(u"Redirecionar para página"),
        null=True, blank=True,
        related_name='redirected_from')
    redirect_to_url = models.URLField(
        verbose_name=_(u"Redirecionar para esta URL"), blank=True)

    class Meta:
        abstract = True
