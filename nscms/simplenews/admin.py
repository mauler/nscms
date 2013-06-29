#-*- coding:utf-8 -*-

from django.contrib.admin import site, ModelAdmin

from .models import SimpleNews


class SimpleNewsAdmin(ModelAdmin):
    date_hierarchy = "publish_date"
    search_fields = ("title", "description", "content",)
    list_filter = ("published", )
    list_display = (
        "title", "published", "publish_date",)
    fieldsets = (
        (None,
        {"fields": ("title", "tags", "image", "description", "content",)}),
        (u"Publicação",
            {"fields": ("published", "publish_date", "expire_date",)}),
        )


site.register(SimpleNews, SimpleNewsAdmin)
