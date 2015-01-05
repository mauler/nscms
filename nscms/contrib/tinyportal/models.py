from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey
from nscms.base.content.models import ContentModel, SimpleContentModel
from sorl.thumbnail import ImageField


class Channel(MPTTModel, SimpleContentModel):
    parent = TreeForeignKey('self',
                            blank=True,
                            null=True,
                            related_name='children')

    image = ImageField(
        blank=True,
        upload_to="channels",
        verbose_name=_("Image"),
    )


class ContainerModel(ContentModel):
    channel = TreeForeignKey('Channel')

    class Meta:
        abstract = True


class Container(ContainerModel):
    pass
