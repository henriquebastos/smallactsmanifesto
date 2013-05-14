# coding: utf-8
from django.test import TestCase
from ..models import Signatory


class SignatoryModelTest(TestCase):
    def setUp(self):
        self.object = Signatory.objects.create(
            name='Henrique Bastos', email='henrique@bastos.net',
            url='', location='')

    def test_create(self):
        'Create one Signatory.'
        self.assertEqual(1, self.object.pk)

    def test_generate_confirmation_key(self):
        self.assertEqual('70698fbcf410f6538a6367d9a6260d95d366e9c5',
                         self.object.confirmation_key)

    def test_get_confirm_url(self):
        'Returns the absolute email confirmation url.'
        url = 'http://smallactsmanifesto.org/signup/confirm/70698fbcf410f6538a6367d9a6260d95d366e9c5/'
        self.assertEqual(url, self.object.get_confirm_url())

    def test_allow_blank_url(self):
        'URL can be blank.'
        self.assertEqual('', self.object.url)

    def test_order(self):
        'Default order must be by name and signed_at.'
        self.assertListEqual(['name', 'signed_at'],
                             Signatory._meta.ordering)
