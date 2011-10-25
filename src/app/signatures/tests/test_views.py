from datetime import datetime as dt
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core import mail


__all__ = ['TestViews']

class TestViews(TestCase):
    def test_render_signup_form(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'signatures/form.html')

    def test_valid_form_signup(self):
        post_data = {
            'name': 'Henrique Bastos',
            'email': 'henrique@bastos.net',
            'url': 'http://henriquebastos.net',
            'location': 'Rio de Janeiro/Brazil',
        }
        response = self.client.post(reverse('signup'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signatures/signed.html')

    def test_resubmit_form_signup(self):
        from signatures.models import Signatory
        post_data = {
            'name': 'Henrique Bastos',
            'email': 'henrique@bastos.net',
            'url': 'http://henriquebastos.net',
            'location': 'Rio de Janeiro/Brazil',
        }
        s = Signatory.objects.create(**post_data)
        self.assertEquals(len(mail.outbox), 0)
        response = self.client.post(reverse('signup'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signatures/signed.html')
        self.assertEquals(len(mail.outbox), 1)

    def test_fail_form_without_valid_email(self):
        post_data = {
            'name': 'Henrique Bastos',
            'email': 'henrique',
        }
        response = self.client.post(reverse('signup'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signatures/form.html')

