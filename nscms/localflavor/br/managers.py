#!/usr/bin/env python
#-*- coding:utf-8 -*-

import datetime

from django.db.models import Q
from django.db import models


# Thanks to http://djangosnippets.org/snippets/562/


class BRPublisherModelQuerySet(models.query.QuerySet):

    def publicados(self):
        now = datetime.datetime.now()
        return self.filter(
            Q(publicado=True),
            Q(data_publicacao__lte=now),
            Q(data_expiracao__isnull=True) | Q(data_expiracao__gt=now))


class BRPublisherModelManager(models.Manager):
    queryset_class = BRPublisherModelQuerySet

    def get_query_set(self):
#        model = models.get_model('news', 'BRPublisherModelItem')
#        if self.model._meta.abstract:
#            return models.query.QuerySet(self.model)
#        else:
        return self.queryset_class(self.model)

    def publicados(self):
        return self.get_query_set().publicados()

#    def __getattr__(self, attr, *args):
#        if attr in ("publicados", ):
#            return getattr(self.get_query_set(), attr, *args)
#        else:
#            return super(BRPublisherModelManager, self).__getattr__(
#                attr, *args)
#            return getattr(self.__class__, attr, *args)
