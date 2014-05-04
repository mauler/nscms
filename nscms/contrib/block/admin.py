#-*- coding:utf-8 -*-

from django.conf import settings
from django.contrib import admin

from .forms import BlockForm
from .models import Block


def get_modeladmin_class():
    if 'reversion' in settings.INSTALLED_APPS:
        import reversion
        return reversion.VersionAdmin
    else:
        admin.ModelAdmin


class BlockAdmin(get_modeladmin_class()):
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
    form = BlockForm

admin.site.register(Block, BlockAdmin)
