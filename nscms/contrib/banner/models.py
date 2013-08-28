#-*- coding:utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from nscms.base.content.models import ContentModel, SimpleContentModel
from nscms.helpers.upload import UploadTo


class Section(SimpleContentModel):

    class Meta(SimpleContentModel.Meta): 
        abstract = False
        verbose_name = _(u'Section')
        verbose_name_plural = _(u'Sections')       
    
    
class Banner(ContentModel): 
    section = models.ForeignKey(
        "Section", verbose_name=_(u'Section'), blank=True, null=True)
    image = models.ImageField(_(u'Image'), upload_to=UploadTo('banners'))
    url = models.URLField(u"URL")

