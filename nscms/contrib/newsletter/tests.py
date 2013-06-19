#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.core.urlresolvers import reverse
from django.test.client import Client
from django.test import TestCase

from .models import Subscription


class NewsletterTestCase(TestCase):

    def test_optin(self):
        email = u"user@domain.com"
        client = Client()
        url = reverse("newsletter:optin")
        response = client.get(url, {'email': email})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            Subscription.objects.all(), ['<Subscription: user@domain.com>'])
