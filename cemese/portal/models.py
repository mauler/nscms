#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string

from ckeditor.fields import RichTextField
from feincms.module.page.models import Page
from feincms.content.image.models import ImageContent
from feincms.content.richtext.models import RichTextContent
from feincms.content.section.models import SectionContent
from taggit.managers import TaggableManager

from cemese.db.models import ContentModel


from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^ckeditor\.fields\.RichTextField"])

Page.register_extensions('cemese.portal.page.extensions.tags',
                         'datepublisher',
                         'changedate',
                         'seo')

#from feincms.content.application.models import ApplicationContent
#from feincms.module.page.models import Page

#Page.create_content_type(ApplicationContent, APPLICATIONS=(
#    ('news.urls', 'News application'),
#    ))


Page.create_content_type(RichTextContent)

#Page.create_content_type(ImageContent, POSITION_CHOICES=(
#    ('block', _('block')),
#    ('left', _('left')),
#    ('right', _('right')),
#))

#from cemese.portal.news.models import News

#def Page_get_news_published(self, count=10):
#    qs = News.objects.published(order_by=None)
#    qs = qs.filter(tags__pk__in=[i.pk for i in self.tags.all()])
#    return qs[:count]

#Page.get_news_published = Page_get_news_published

