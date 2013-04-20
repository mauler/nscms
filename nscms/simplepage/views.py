#-*- coding:utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404

from nscms.simplepage.models import SimplePage


def page(request, url, template_name=u"site/pages/page.html", context={}):
    parts = url.split("/")
    qs = SimplePage.objects.filter(published=True)
    root = parts[0]
    nodes = parts[1:]
    current = get_object_or_404(qs, slug=root, parent__isnull=True)
    for slug in nodes:
        current = get_object_or_404(qs, slug=slug, parent=current)
    page = current
    if page.redirect_to_url:
        return redirect(page.redirect_to_url)

    if page.redirect_to is not None:
        return redirect(page.redirect_to.get_absolute_url())

    context.update({
        'page': page,
    })
    return render(request, template_name, context)
