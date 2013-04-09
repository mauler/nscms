#-*- coding:utf-8 -*-

from django.forms import *

from taggit.models import Tag
from taggit.forms import TagField
from taggit.utils import edit_string_for_tags, parse_tags


class TagSelectMultiple(CheckboxSelectMultiple):
    def render(self, name, value, attrs=None):
        choices = [(i.name, i.name) for i in Tag.objects.all().order_by("name")]
        if value and value is not None and not isinstance(value, (basestring, list)):
            value = edit_string_for_tags([o.tag for o in value.select_related("tag")])
            value = parse_tags(value)
        return super(TagSelectMultiple, self).render(name, value, attrs, choices=choices)


class CheckboxTagField(TagField):
    widget = TagSelectMultiple

    def clean(self, value):
        value = ','.join(["\"%s\"" % i for i in value])
        return super(CheckboxTagField, self).clean(value)
