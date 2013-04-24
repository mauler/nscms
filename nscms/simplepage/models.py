#-*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from nscms.base.simplepage.models import SimplePageModel


class SimplePage(SimplePageModel):

    class Meta:
        ordering = ['-created']
        verbose_name = _(u"Página")
        verbose_name_plural = _(u"Páginas")
        abstract = False

    def get_absolute_url(self):
        if self.redirect_to_url:
            return self.redirect_to_url

        if self.redirect_to:
            return self.redirect_to.get_absolute_url()

        parts = [self.slug]
        page = self
        while page.parent is not None:
            page = page.parent
            parts.insert(0, page.slug)
        return u"/%s/" % u"/".join(parts)
    get_absolute_url.short_description = u"URL"
