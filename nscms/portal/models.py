#-*- coding:utf-8 -*-

from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent


from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^ckeditor\.fields\.RichTextField"])

Page.register_extensions('nscms.portal.page.extensions.tags',
                         'datepublisher',
                         'changedate',
                         'seo')


Page.create_content_type(RichTextContent)
