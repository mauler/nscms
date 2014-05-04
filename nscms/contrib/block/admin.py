#-*- coding:utf-8 -*-

from django.contrib import admin

from .models import Block


class BlockAdmin(admin.ModelAdmin):
    list_display = (
        "title", "slug", "is_template", "published", "publish_date")
    list_filter = ("is_template", "published", )
    search_fields = ("title", "slug", "content", )
    fieldsets = (
        (None, {'fields': ['title', 'content']}),
        (None, {'fields': ['is_template']}),
        (u"Publicação", {'fields': [
            'published', ('publish_date', 'expire_date')]}),
    )

admin.site.register(Block, BlockAdmin)
