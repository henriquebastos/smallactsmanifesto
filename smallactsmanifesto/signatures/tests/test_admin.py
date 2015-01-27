# coding: utf-8
from django.test import TestCase
from django.contrib import admin
from mock import Mock
from smallactsmanifesto.signatures.admin import SignatoryAdmin
from smallactsmanifesto.signatures.models import Signatory


class SignatoryAdminTest(TestCase):
    def setUp(self):
        self.admin = SignatoryAdmin(Signatory, admin.site)
        Signatory.objects.create(
            name='Henrique Bastos', email='henrique@bastos.net',
            url='', location='')

    def test_has_action(self):
        self.assertIn('activate', self.admin.actions)

    def test_activate(self):
        self.admin.activate(Mock(), Signatory.objects.all())

        assert Signatory.objects.filter(is_active=True).count() == 1
