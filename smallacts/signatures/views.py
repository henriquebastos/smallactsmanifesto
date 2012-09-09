# coding: utf-8
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse as r
from django.template.loader import render_to_string
from django.views.generic import CreateView
from django.views.generic import TemplateView
from .forms import SignupForm


class SignupView(CreateView):
    "Shows the signup form and saves it's submission."
    form_class = SignupForm
    template_name = 'signatures/signup_form.html'
    template_email_subject = 'signatures/signup_email_subject.txt'
    template_email_body = 'signatures/signup_email_body.txt'

    def get_success_url(self):
        return r('signatures:success')

    def form_valid(self, form):
        response = super(SignupView, self).form_valid(form)
        self.send_confirmation_email()
        return response

    def send_confirmation_email(self):
        """
        Sends the signup confirmation email to the Signatory.
        He will only be listed after access the confirmation link.
        """
        context = { object: self.object }
        subject = render_to_string(self.template_email_subject, context)
        message = render_to_string(self.template_email_body, context)

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
                  [self.object.email, settings.DEFAULT_FROM_EMAIL])


signup = SignupView.as_view()


class SignupSuccessView(TemplateView):
    'Shows a success page after user has signedup.'
    template_name='signatures/signup_success.html'

success = SignupSuccessView.as_view()

def confirm(request):
    return direct_to_template(request, 'signatures/confirmed.html')
