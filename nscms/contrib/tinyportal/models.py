
from mptt.models import MPTTModel, TreeForeignKey
from nscms.base.content.models import ContentModel, SimpleContentModel


class Channel(MPTTModel, SimpleContentModel):
    parent = TreeForeignKey('self',
                            blank=True,
                            null=True,
                            related_name='children')


class ContainerModel(ContentModel):
    channel = TreeForeignKey('Channel')

    class Meta:
        abstract = True


class Container(ContainerModel):
    pass
