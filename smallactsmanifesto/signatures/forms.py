# coding: utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _
from captcha.fields import ReCaptchaField
from .models import Signatory
from .utils import mark_safe_lazy as safe


HELP_CAPTCHA = safe(_('Just a small act to prevent spam. <em>Sorry about this!</em>'))


class SignupForm(forms.ModelForm):
    captcha = ReCaptchaField(attrs={'theme' : 'white'}, help_text=HELP_CAPTCHA)

    class Meta:
        model = Signatory
        fields = ('name', 'email', 'url', 'location')

    def save(self, commit=True):
        try:
            return Signatory.objects.get(email=self.instance.email)
        except Signatory.DoesNotExist:
            pass

        return super(SignupForm, self).save(commit)
