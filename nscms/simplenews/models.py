#-*- coding:utf-8 -*-

from django.core.urlresolvers import reverse

from nscms.base.simplenews.models import BaseNews


class SimpleNews(BaseNews):

    def get_absolute_url(self):
        return reverse(
            "noticias_interna", args=(self.publish_date.strftime("%Y"),
            self.publish_date.strftime("%m"),
            self.publish_date.strftime("%d"),
            self.slug))
