#-*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from nscms.base.simplenews.models import SimpleNewsModel

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


class SimpleNews(SimpleNewsModel):
    content = RichTextField()
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ['-publish_date']
        verbose_name = _(u"Notícia")
        verbose_name_plural = _(u"Notícias")
        abstract = False

    def related_by_tags(self, count=10):
        qs = self.__class__.objects.published(order_by=None)
        qs = qs.filter(
            tags__pk__in=[i.pk for i in self.tags.all()]).exclude(pk=self.id)
        return qs[:count]
