# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from ..models import Signatory


class ConfirmViewTest(TestCase):
    def setUp(self):
        obj = Signatory.objects.create(name='Henrique Bastos',
                                       email='henrique@bastos.net')

        self.resp = self.client.get(r('signatures:confirm',
                                      args=[obj.confirmation_key]))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'signatures/signup_confirm.html')

    def test_activated(self):
        'After confirmed, Signatory must be active.'
        self.assertTrue(Signatory.objects.filter(is_active=True).exists())


class ConfirmViewNotFound(TestCase):
    def test_404(self):
        Signatory.objects.create(name='Henrique Bastos',
                                 email='henrique@bastos.net')

        response = self.client.get(r('signatures:confirm', args=['0']))
        self.assertEqual(404, response.status_code)
