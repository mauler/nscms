# -*- coding:utf-8 -*-

# Core Django imports
from django.contrib import admin
from django.utils.translation import ugettext as _

# Thirdy Apps imports
from feincms.admin import tree_editor

# Realative imports of the 'app-name' package
from nscms.simplepage.models import SimplePage


class SimplePageAdmin(tree_editor.TreeEditor):
    list_display = (
        "title",
        "slug",
        "get_absolute_url",
        "published",
        "redirect_to",
        "redirect_to_url",
    )

    search_fields = (
        "title",
        "slug",
        "content",
    )

    fieldsets = (
        (
            None,
            {
                'fields': [
                    'parent',
                    'title',
                    'content'
                ]
            }
        ),
        (
            _(u"Publicação"),
            {
                'fields': [
                    'published',
                    (
                        'publish_date',
                        'expire_date'
                    )
                ]
            }
        ),
        (
            _("Meta data"),
            {
                "fields": [
                    "meta_title",
                    "slug",
                    "description",
                    "keywords",
                ],
                "classes": ("collapse-closed",)
            }
        ),
        (
            u"Redirecionar",
            {
                'description': (
                    "Caso uma página não possua conteúdo é possível "
                    "definir um redirecionamento. A prioridade de "
                    "redirecionamento segue a ordem abaixo. "
                ),
                'fields': ['redirect_to', "redirect_to_url"],
                'classes': ['grp-collapse grp-closed']
            }
        ),
    )

admin.site.register(SimplePage, SimplePageAdmin)
