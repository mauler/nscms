#-*- coding:utf-8 -*-

from django.contrib.admin import ModelAdmin, site

from .models import Section, Banner


class SectionAdmin(ModelAdmin):
    pass


site.register(Section, SectionAdmin)


class BannerAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': [
            'section', 'title', 'image', 'url']}),
        (u"Publicação", {'fields': [
            'published', ('publish_date', 'expire_date', )]}),
    )
    list_display = ("title", "url", "section", "published", "publish_date", )
    list_filter = ("section", "published", "publish_date", )


site.register(Banner, BannerAdmin)
