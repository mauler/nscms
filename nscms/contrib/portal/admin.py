from django.contrib.admin import site

from .models import Channel, Container


site.register(Channel)
site.register(Container)
