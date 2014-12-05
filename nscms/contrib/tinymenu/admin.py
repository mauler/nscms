from django.contrib.admin import site

from mptt.admin import MPTTModelAdmin

from .models import Node


site.register(Node, MPTTModelAdmin)
