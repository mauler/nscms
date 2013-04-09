#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.db.models import Q
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField
from django_extensions.db.fields import *

import datetime


CEMESE_CONTENT_TITLE_LENGTH = getattr(settings,
                                      "CEMESE_CONTENT_TITLE_LENGTH",
                                      255)


class PublisherModelManager(models.Manager):
    """ PublisherModelManager
    Manager to return instances of ActivatorModel:
    SomeModel.objects.published() / .expired()
    """
    def published(self, order_by=None):
        """ Returns published instances of PublisherModel:
            SomeModel.objects.published() """
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
        """ Returns published instances of PublisherModel:
            SomeModel.objects.published() """
        now = datetime.datetime.now()
        return super(PublisherModelManager, self).get_query_set().filter(
            published=True,
            publish_date__gt=now
        ).order_by("publish_date")

    def expired(self):
        """ Returns expired instances of PublisherModel:
            SomeModel.objects.expired() """
        now = datetime.datetime.now()
        return super(PublisherModelManager, self).get_query_set().filter(
            expire_date__lt=now
        ).order_by("publish_date")


class ContentModel(models.Model):
    title = models.CharField(
        _('title'), max_length=CEMESE_CONTENT_TITLE_LENGTH)
    slug = AutoSlugField(
        _('slug'), populate_from='title', overwrite=True,
        max_length=CEMESE_CONTENT_TITLE_LENGTH, editable=False)
    description = models.TextField(_('description'), blank=True, null=True)

    created = CreationDateTimeField(_('created'))
    modified = ModificationDateTimeField(_('modified'))

    def __unicode__(self):
        return self.title

    class Meta:
        abstract = True


class SimpleContentModel(models.Model):
    title = models.CharField(
        _('title'), max_length=CEMESE_CONTENT_TITLE_LENGTH)
    slug = AutoSlugField(
        _('slug'), populate_from='title',
        overwrite=True, max_length=CEMESE_CONTENT_TITLE_LENGTH,
        editable=False)
    created = CreationDateTimeField(_('created'))
    modified = ModificationDateTimeField(_('modified'))

    def __unicode__(self):
        return self.title

    class Admin(admin.ModelAdmin):
        pass

    class Meta:
        abstract = True
        ordering = ("title", )


class PersonModel(models.Model):
    name = models.CharField(_('name'), max_length=255)
    slug = AutoSlugField(
        _('slug'), populate_from='name', overwrite=True,
        max_length=255, editable=False)
    created = CreationDateTimeField(_('created'))
    modified = ModificationDateTimeField(_('modified'))

    def __unicode__(self):
        return self.name

    class Admin(admin.ModelAdmin):
        pass

    class Meta:
        abstract = True
        ordering = ("name", )


class CreationModificationModel(models.Model):
    created = CreationDateTimeField(_('created'))
    modified = ModificationDateTimeField(_('modified'))

    class Meta:
        abstract = True
        ordering = ("-created", "-modified", )


DateContentModel = CreationModificationModel


class PublisherModel(models.Model):
    """ PublisherModel
    An abstract base class model that provides publish and expired fields.
    """

    published = models.BooleanField(
        _('published'), default=False)
    publish_date = models.DateTimeField(
        blank=True, null=True,
        help_text=_('keep empty for an immediate publication'),
        verbose_name=_('publish date'))
    expire_date = models.DateTimeField(
        blank=True, null=True,
        help_text=_('keep empty for indefinite expiration'),
        verbose_name=_('expire date'))

    objects = PublisherModelManager()

    class Meta:
        abstract = True
        ordering = ("-publish_date", "-published", )

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


ADMIN_FIELDSET_PUBLISHING = (
    _(u"Publicação"),
    {"fields": ("published", "publish_date", "expire_date", )})


class ContentModel(ContentModel, PublisherModel):
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

    class Meta(PublisherModel.Meta):
        abstract = True


class TextContentModel(ContentModel):
    body = RichTextField(verbose_name=_(u"Corpo"))

    class Admin(ContentModel.Admin):
        fieldsets = (
            (None, {"fields": ("title", "description", "body", )}),
            ADMIN_FIELDSET_PUBLISHING,
        )

    class Meta(ContentModel.Meta):
        abstract = True


class PTBRSimpleContentModel(models.Model):
    title = models.CharField(_(u'Título'), max_length=255)
    slug = AutoSlugField(
        _('slug'), populate_from='titulo',
        overwrite=True, max_length=255, editable=False)

    created_at = CreationDateTimeField(_(u'Criado em'))
    changed_at = ModificationDateTimeField(_(u'Modificado em'))

    def __unicode__(self):
        return self.title

    class Admin(admin.ModelAdmin):
        pass

    class Meta:
        abstract = True
        ordering = ("titulo", )


try:
    import south
except ImportError:
    pass
else:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^ckeditor\.fields\.RichTextField"])
