#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.core.urlresolvers import reverse

from cemese.portal.base.news.models import BaseNews
from photologue.models import ImageModel

class News(BaseNews, ImageModel):

    def get_absolute_url(self):
        return reverse("noticias_interna", args=(self.publish_date.strftime("%Y"),
                                                 self.publish_date.strftime("%m"),
                                                 self.publish_date.strftime("%d"),
                                                 self.slug))

