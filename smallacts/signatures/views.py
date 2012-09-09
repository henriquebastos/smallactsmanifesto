# coding: utf-8
from django.core.urlresolvers import reverse as r
from django.views.generic import CreateView
from django.views.generic import TemplateView
from .forms import SignupForm
from .utils import send_email_confirmation


class SignupView(CreateView):
    "Shows the signup form and saves it's submission."
    form_class = SignupForm
    template_name = 'signatures/signup_form.html'

    def get_success_url(self):
        return r('signatures:success')

    def form_valid(self, form):
        response = super(SignupView, self).form_valid(form)
        send_email_confirmation(self.object)
        return response

signup = SignupView.as_view()


class SignupSuccessView(TemplateView):
    'Shows a success page after user has signedup.'
    template_name='signatures/signup_success.html'

success = SignupSuccessView.as_view()

def confirm(request):
    return direct_to_template(request, 'signatures/confirmed.html')
