#-*- coding:utf-8 -*-

from django.contrib import admin

from .models import Block


class BlockAdmin(admin.ModelAdmin):
    list_display = (
        "title", "slug", "published", "publish_date")
    search_fields = ("title", "slug", "content", )
    fieldsets = (
        (None, {'fields': ['title', 'content']}),
        (u"Publicação", {'fields': [
            'published', ('publish_date', 'expire_date')]}),
    )

admin.site.register(Block, BlockAdmin)
