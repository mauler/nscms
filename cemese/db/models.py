#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q

from ckeditor.fields import RichTextField
from django_extensions.db.fields import *

import datetime


class PublisherModelManager(models.Manager):
    """ PublisherModelManager
    Manager to return instances of ActivatorModel: SomeModel.objects.published() / .expired()
    """
    def published(self, order_by=None):
        """ Returns published instances of PublisherModel: SomeModel.objects.published() """
        now = datetime.datetime.now()
        qset = super(PublisherModelManager, self).filter(
            Q(published=True),
            Q(publish_date__lte=now),
            Q(expire_date__isnull=True) | Q(expire_date__gt=now)
        )
        if order_by is not None:
            qset = qset.order_by(order_by)
        return qset

    def unpublished(self):
        """ Returns published instances of PublisherModel: SomeModel.objects.published() """
        now = datetime.datetime.now()
        return super(PublisherModelManager, self).get_query_set().filter(
            published=True,
            publish_date__gt=now
        ).order_by("publish_date")

    def expired(self):
        """ Returns expired instances of PublisherModel: SomeModel.objects.expired() """
        now = datetime.datetime.now()
        return super(PublisherModelManager, self).get_query_set().filter(
            expire_date__lt=now
        ).order_by("publish_date")

class _ContentModel(models.Model):

    title = models.CharField(_('title'), max_length=255)
    slug = AutoSlugField(_('slug'), populate_from='title', overwrite=True)
    description = models.TextField(_('description'), blank=True, null=True)

    created = CreationDateTimeField(_('created'))
    modified = ModificationDateTimeField(_('modified'))

    def __unicode__(self):
        return self.title

    class Meta:
        abstract = True

class SimpleContentModel(models.Model):

    title = models.CharField(_('title'), max_length=255)
    slug = AutoSlugField(_('slug'), populate_from='title', overwrite=True)

    created = CreationDateTimeField(_('created'))
    modified = ModificationDateTimeField(_('modified'))

    def __unicode__(self):
        return self.title

    class Admin(admin.ModelAdmin):
        pass

    class Meta:
        abstract = True
        ordering = ("title", )


class DateContentModel(models.Model):
    created = CreationDateTimeField(_('created'))
    modified = ModificationDateTimeField(_('modified'))

    class Meta:
        abstract = True
        ordering = ("-created", "-modified", )


class PublisherModel(models.Model):
    """ PublisherModel
    An abstract base class model that provides publish and expired fields.
    """

    published = models.BooleanField(_('published'), default=False)
    publish_date = models.DateTimeField(blank=True, null=True,
                                        help_text=_('keep empty for an immediate publication'),
                                        verbose_name=_('publish date'))
    expire_date = models.DateTimeField(blank=True, null=True,
                                       help_text=_('keep empty for indefinite expiration'),
                                       verbose_name=_('expire date'))

    objects = PublisherModelManager()

    class Meta:
        abstract = True
        ordering = ("-published", )

    def is_published(self):
        now = datetime.datetime.now()
        return self.published and \
               self.publish_date <= now and \
               (self.expire_date is None or self.expire_date > now)

    def save(self, *args, **kwargs):
        if not self.publish_date:
            self.publish_date = datetime.datetime.now()
        super(PublisherModel, self).save(*args, **kwargs)

ADMIN_FIELDSET_TITLE = (None, {"fields": ("title", "description", )})
ADMIN_FIELDSET_PUBLISHING = (_(u"Publicação"), {"fields": ("published", "publish_date", "expire_date", )})

class ContentModel(_ContentModel, PublisherModel):
    ADMIN_FIELDSET_TITLE = ADMIN_FIELDSET_TITLE
    ADMIN_FIELDSET_PUBLISHING = ADMIN_FIELDSET_PUBLISHING

    class Admin(admin.ModelAdmin):
        date_hierarchy = 'publish_date'
        fieldsets = (
            ADMIN_FIELDSET_TITLE,
            ADMIN_FIELDSET_PUBLISHING,
        )
        list_display = ("title", "publish_date", "published", )
        list_filter = ("published", )
        search_fields = ("title", "description", )

    class Meta:
        abstract = True

class TextContentModel(ContentModel):
    body = RichTextField()

    class Admin(ContentModel.Admin):
        fieldsets = (
            (None, {"fields": ("title", "description", "body", )}),
            ADMIN_FIELDSET_PUBLISHING,
        )


    class Meta:
        abstract = True

