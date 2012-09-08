# coding: utf-8
from django.views.generic import CreateView
from .forms import SignupForm


class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'signatures/signup_form.html'

signup = SignupView.as_view()
