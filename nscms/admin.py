from django.utils.translation import ugettext_lazy as _


class ViewOnSiteMixin:
    view_on_site_text = None
    view_on_site_target = '_blank'

    def col_view_on_site(self, obj):
        if hasattr(obj, 'get_absolute_url'):
            url = obj.get_absolute_url()
            text = self.view_on_site_text or url
            args = (url, self.view_on_site_target, text)
            src = '<a href="%s" target="%s">%s</a>' % args
            return src
    col_view_on_site.short_description = _("View on site")
    col_view_on_site.allow_tags = True
