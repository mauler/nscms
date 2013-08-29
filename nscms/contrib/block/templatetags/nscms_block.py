from django import template

from classytags.core import Tag, Options
from classytags.arguments import Argument

from ..models import Block


register = template.Library()


class RenderBlock(Tag):
    name = 'render_block'
    options = Options(
        Argument('title'),
    )

    def render_tag(self, context, title):
        qs = Block.objects.published().filter(title=title)
        if qs.exists():
            block = qs[0]
        else:
            block = Block()
            block.title = title
            block.published = True
            block.save()
        return block.content


register.tag(RenderBlock)
