from django.contrib.admin import site

from mptt.admin import MPTTModelAdmin

from .models import Node


class NodeAdmin(MPTTModelAdmin):
    search_fields = ("title", )


site.register(Node, NodeAdmin)
