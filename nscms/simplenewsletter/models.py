#-*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from nscms.base.simplenewsletter.models import SimpleNewsletterModel


class SimpleNewsletter(SimpleNewsletterModel):

    class Meta:
        ordering = ['-created']
        verbose_name = _(u"Inscrição")
        verbose_name_plural = _(u"Inscrições")
        abstract = False
