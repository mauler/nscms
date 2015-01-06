from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey
from nscms.base.content.models import ContentModel, SimpleContentModel
from sorl.thumbnail import ImageField


TINYPORTAL_CHANNEL_VERBOSE_NAME = \
    getattr(settings, "TINYPORTAL_CHANNEL_VERBOSE_NAME", "Channel")
TINYPORTAL_CHANNEL_VERBOSE_NAME_PLURAL = \
    getattr(settings, "TINYPORTAL_CHANNEL_VERBOSE_NAME_PLURAL", "Channels")


class Channel(MPTTModel, SimpleContentModel):
    parent = TreeForeignKey('self',
                            blank=True,
                            null=True,
                            related_name='children',
                            verbose_name=_("Parent"))

    image = ImageField(
        blank=True,
        upload_to="channels",
        verbose_name=_("Image"),
    )

    class Meta:
        verbose_name = _(TINYPORTAL_CHANNEL_VERBOSE_NAME)
        verbose_name_plural = _(TINYPORTAL_CHANNEL_VERBOSE_NAME_PLURAL)


class ContainerModel(ContentModel):
    channel = TreeForeignKey('Channel')

    class Meta:
        abstract = True


class Container(ContainerModel):
    pass
