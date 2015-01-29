from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from colorful.fields import RGBColorField
from mptt.models import MPTTModel, TreeForeignKey
from nscms.base.content.models import ContentModel, SimpleContentModel
from sorl.thumbnail import ImageField
from taggit.managers import TaggableManager


TINYPORTAL_CHANNEL_TAGGIT = \
    getattr(settings, "TINYPORTAL_CHANNEL_TAGGIT", True)
TINYPORTAL_CHANNEL_VERBOSE_NAME = \
    getattr(settings, "TINYPORTAL_CHANNEL_VERBOSE_NAME", "Channel")
TINYPORTAL_CHANNEL_VERBOSE_NAME_PLURAL = \
    getattr(settings, "TINYPORTAL_CHANNEL_VERBOSE_NAME_PLURAL", "Channels")
TINYPORTAL_CONTAINER_TAGGIT = \
    getattr(settings, "TINYPORTAL_CONTAINER_TAGGIT", True)


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

    alternative_color_hex = RGBColorField(
        default="#000000",
        verbose_name=_("Cor Alternativa"),
    )

    tags = TaggableManager()

    class Meta:
        verbose_name = _(TINYPORTAL_CHANNEL_VERBOSE_NAME)
        verbose_name_plural = _(TINYPORTAL_CHANNEL_VERBOSE_NAME_PLURAL)


def channel_pre_save(sender, instance, *args, **kwargs):
    if instance.alternative_color_hex and not \
            instance.alternative_color_hex.startswith('#'):
        instance.alternative_color_hex = "#%s" % instance.alternative_color_hex


class ContainerModel(ContentModel):
    channel = TreeForeignKey('Channel')
    tags = TaggableManager()

    class Meta:
        abstract = True


class Container(ContainerModel):
    pass
