from django.template import Template
from django import template

from classytags.core import Tag, Options
from classytags.arguments import Argument

from ..models import Block


register = template.Library()


class RenderBlock(Tag):
    name = 'render_block'
    options = Options(
        Argument('title'),
        'as',
        Argument('varname', required=False, resolve=False)
    )

    def render_tag(self, context, title, varname):
        qs = Block.objects.published().filter(title=title)
        if qs.exists():
            block = qs[0]
        else:
            block = Block()
            block.title = title
            block.published = True
            block.save()

        if block.is_template:
            output = Template(block.content).render(context)
        else:
            output = block.content

        if varname:
            context[varname] = output
            return ''
        else:
            return output


register.tag(RenderBlock)
