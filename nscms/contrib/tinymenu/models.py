from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
from nscms.base.content.models import SimpleContentModel


class Node(MPTTModel, SimpleContentModel):
    parent = TreeForeignKey('self',
                            blank=True,
                            null=True,
                            related_name='children')
    url = models.CharField(max_length=100, blank=True)
