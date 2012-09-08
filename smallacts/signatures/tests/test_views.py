# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from ..forms import SignupForm


class SignupViewTest(TestCase):
    'Signup GET tests.'
    def setUp(self):
        self.resp = self.client.get(r('signatures:signup'))

    def test_get(self):
        'GET must return 200 as status code.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Signup must be rendered with signatures/signup_form.html'
        self.assertTemplateUsed(self.resp, 'signatures/signup_form.html')

    def test_form(self):
        'SignupForm must be in context.'
        form = self.resp.context['form']
        self.assertIsInstance(form, SignupForm)

    def test_html(self):
        'HTML must contain expected inputs.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, "type='hidden'")
        self.assertContains(self.resp, 'type="text"', 4)
        self.assertContains(self.resp, 'type="submit"')

