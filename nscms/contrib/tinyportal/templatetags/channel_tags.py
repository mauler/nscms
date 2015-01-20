from django import template

from classytags.arguments import Argument
from classytags.core import Options
from classytags.helpers import AsTag


register = template.Library()


class FilterInChannelTree(AsTag):
    name = 'filter_in_channel_tree'
    options = Options(
        Argument('queryset'),
        Argument('channel'),
        'as',
        Argument('varname', required=False, resolve=False, default="objects")
    )

    def get_value(self, context, queryset, channel):
        return queryset.filter(
            channel__tree_id=channel.tree_id,
            channel__lft__gte=channel.lft)


register.tag(FilterInChannelTree)
