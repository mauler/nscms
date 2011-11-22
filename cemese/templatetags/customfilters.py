from cemese_tags import *
from django.conf import settings


@register.filter
def url(filepath):
    return settings.MEDIA_URL + filepath

