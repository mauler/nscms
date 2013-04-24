#-*- coding:utf-8 -*-

from django.contrib import admin

from feincms.admin import tree_editor

from nscms.simplepage.models import SimplePage


class SimplePageAdmin(tree_editor.TreeEditor):
    list_display = (
        "title", "slug", "get_absolute_url", "published", "redirect_to",
        "redirect_to_url", )
    search_fields = ("title", "slug", "content", )
    fieldsets = (
        (None, {'fields': ['parent', 'title', 'content']}),
        (u"Publicação", {'fields': [
            'published', ('publish_date', 'expire_date')]}),
        (u"Redirecionar", {
            'description': "Caso uma página não possua conteúdo é possível " \
            "definir um redirecionamento. A prioridade de redirecionamento " \
            "segue a ordem abaixo.",
            'fields': ['redirect_to', "redirect_to_url"],
            'classes': ['grp-collapse grp-closed']}),
    )

admin.site.register(SimplePage, SimplePageAdmin)
