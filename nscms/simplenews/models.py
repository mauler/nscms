#-*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

from nscms.base.db.models import ContentModel


class NewsModel(ContentModel):
    body = RichTextField()
    tags = TaggableManager(blank=True)

    class Admin(ContentModel.Admin):
        date_hierarchy = "publish_date"
        search_fields = ("title", "description", "body",)
        list_filter = ("published", )
        list_display = (
            "title", "published", "publish_date",)
        fieldsets = (
            (None,
             {"fields": ("title", "tags", "description", "body",)}),
            (_(u"Publicação"),
             {"fields": ("published", "publish_date", "expire_date",)}),
        )

    class Meta:
        ordering = ['-publish_date']
        verbose_name = _(u"Notícia")
        verbose_name_plural = _(u"Notícias")
        abstract = True

    def related_by_tags(self, count=10):
        qs = self.__class__.objects.published(order_by=None)
        qs = qs.filter(
            tags__pk__in=[i.pk for i in self.tags.all()]).exclude(pk=self.id)
        return qs[:count]

    def get_absolute_url(self):
        return reverse(
            "noticias_interna", args=(self.publish_date.strftime("%Y"),
            self.publish_date.strftime("%m"),
            self.publish_date.strftime("%d"),
            self.slug))
