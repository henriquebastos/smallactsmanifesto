# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r


class SuccessViewTest(TestCase):
    'Signup success GET tests.'
    def setUp(self):
        self.resp = self.client.get(r('signatures:success'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'signatures/signup_success.html')
