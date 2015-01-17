from django.conf import settings
from django.contrib.admin import site

from mptt.admin import MPTTModelAdmin
from .models import Channel, Container


def get_model_admin_class():

    if 'feincms' in settings.INSTALLED_APPS:
        from mptt.admin import FeinCMSModelAdmin
        return FeinCMSModelAdmin

    if 'mptt_tree_editor' in settings.INSTALLED_APPS:
        from mptt_tree_editor.admin import TreeEditor
        return TreeEditor

    if 'django_mptt_admin' in settings.INSTALLED_APPS:
        from django_mptt_admin.admin import DjangoMpttAdmin
        return DjangoMpttAdmin

    return MPTTModelAdmin


class ChannelAdmin(get_model_admin_class()):
    pass


site.register(Channel, ChannelAdmin)


site.register(Container)
