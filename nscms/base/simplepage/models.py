# -*- coding:utf-8 -*-

# Core Django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager

# Thirdy Apps imports
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField

# Realative imports of the 'app-name' package
from nscms.base.content.models import SimpleContentModel, \
    PublisherModel


class MetaData(models.Model):
    u"""
    Classe meta data para prover conteudo de seo
    """
    meta_title = models.CharField(
        verbose_name=_(u'Titulo'),
        null=True,
        blank=True,
        max_length=100,
        help_text=_(u'Titulo opcional usado na tag meta title')
    )
    u"""
    Atributo da classe
    setar a meta tag title no html

    Caracteristicas:
    CharField
    max_length=100
    """

    description = models.TextField(
        verbose_name=_(u'Descrição'),
        blank=True
    )
    u"""
    Atributo da classe
    setar a meta tag de descrição no html

    Caracteristicas:
    TextField
    """

    keywords = TaggableManager()
    u"""
    Atributo da classe
    setar as tags através do pacote django-taggit

    Caracteristicas:
    ManyToMany
    """

    class Meta:
        abstract = True


class SimplePageModel(MPTTModel, SimpleContentModel, PublisherModel):
    u"""
    Classe abstrata com os dados de uma página simples
    de cms
    """
    parent = TreeForeignKey(
        'self',
        verbose_name=_(u"Pai"),
        null=True,
        blank=True,
        related_name='children'
    )

    content = RichTextField(
        verbose_name=_(u"Conteúdo")
    )

    redirect_to = TreeForeignKey(
        'self',
        verbose_name=_(u"Redirecionar para página"),
        null=True,
        blank=True,
        related_name='redirected_from'
    )

    redirect_to_url = models.URLField(
        verbose_name=_(u"Redirecionar para esta URL"),
        blank=True
    )

    class Meta:
        abstract = True
