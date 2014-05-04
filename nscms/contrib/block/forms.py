#-*- coding:utf-8 -*-

from django.conf import settings
from django import forms

from .models import Block


class BlockForm(forms.ModelForm):

    class Meta:
        model = Block
        widgets = {}

        if 'suit' in settings.INSTALLED_APPS:
            from suit.widgets import AutosizedTextarea
            widgets = {
                'content': AutosizedTextarea(
                    attrs={
                        'rows': 10,
                        'class': 'input-xxlarge'}),
            }
