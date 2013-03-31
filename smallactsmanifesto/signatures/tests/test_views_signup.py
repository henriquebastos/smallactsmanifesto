# coding: utf-8
import os
from django.conf import settings
from django.core import mail
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from ..forms import SignupForm
from ..models import Signatory


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
        self.assertContains(self.resp, '<input', 7)
        self.assertContains(self.resp, "type='hidden'")
        self.assertContains(self.resp, 'type="text"', 4)
        self.assertContains(self.resp, 'type="submit"')


class SignupViewPostTest(TestCase):
    'Signup POST success tests.'
    def setUp(self):
        # Needed for testing captcha
        os.environ['RECAPTCHA_TESTING'] = 'True'

        data = dict(name='Henrique Bastos', email='henrique@bastos.net',
                    url='http://henriquebastos.net', location='Brasil',
                    recaptcha_response_field='PASSED')
        self.resp = self.client.post(r('signatures:signup'), data)

    def tearDown(self):
        del os.environ['RECAPTCHA_TESTING']

    def test_post(self):
        'POST must return 302 as status code.'
        self.assertEqual(302, self.resp.status_code)

    def test_redirect_to(self):
        'POST must redirect to /signup/success/.'
        endswith_regex = r('signatures:success') + '$'
        self.assertRegexpMatches(self.resp['Location'], endswith_regex)

    def test_save(self):
        'POST must save the signature.'
        self.assertTrue(Signatory.objects.exists())

    def test_mail(self):
        'POST must send a confirmation email.'
        self.assertEqual(1, len(mail.outbox))

    def test_mail_to_signatory(self):
        'POST must send a confirmation email to the signatory'
        self.assertIn('henrique@bastos.net', mail.outbox[0].to)

    def test_mail_admin(self):
        'POST must send a copy of the feedback email to the admin.'
        self.assertIn(settings.DEFAULT_FROM_EMAIL, mail.outbox[0].to)

    def test_mail_has_name(self):
        self.assertIn('Henrique Bastos', mail.outbox[0].body)

    def test_mail_has_link(self):
        obj = Signatory.objects.get(pk=1)
        self.assertIn(obj.get_confirm_url(), mail.outbox[0].body)


class SingupViewInvalidPostTest(TestCase):
    'Signup POST failure tests.'
    def setUp(self):
        data = dict(name='', email='', url='', location='')
        self.resp = self.client.post(r('signatures:signup'), data)

    def test_post(self):
        'POST must return 200 as status_code.'
        self.assertEqual(200, self.resp.status_code)

    def test_form_errors(self):
        'Errors must be displayed.'
        self.assertTrue(self.resp.context['form'].errors)

    def test_must_not_save(self):
        'Data must not be saved.'
        self.assertFalse(Signatory.objects.exists())


class SignupViewResendConfirmationMailTest(TestCase):
    """
    Given that a signatory already signed up
    When he signup again with the same email
    Then the system only resends the email without saving anything.
    """
    def setUp(self):
        Signatory.objects.create(email='henrique@bastos.net',
             name='dummy', url='dummy', location='dummy')

        data = dict(name='Henrique Bastos', email='henrique@bastos.net')
        self.resp = self.client.post(r('signatures:signup'), data)

    def test_redirect_to(self):
        'POST must redirect to /signup/success/.'
        endswith_regex = r('signatures:success') + '$'
        self.assertRegexpMatches(self.resp['Location'], endswith_regex)

    def test_resend_confirmation_email(self):
        'Email must be sent.'
        self.assertEqual(1, len(mail.outbox))

    def test_do_not_save(self):
        'No new Signatory should be saved.'
        self.assertTrue(1, Signatory.objects.count())

    def test_do_not_update(self):
        'No changes to the previews Signatory should be made.'
        expected = [(1, u'dummy', u'henrique@bastos.net', u'dummy', u'dummy')]
        result = Signatory.objects.values_list('pk', 'name', 'email', 'url', 'location')
        self.assertListEqual(expected, list(result))
