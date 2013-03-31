# coding: utf-8
from django import forms
from captcha.fields import ReCaptchaField
from .models import Signatory


class SignupForm(forms.ModelForm):
    captcha = ReCaptchaField(attrs={'theme' : 'white'})

    class Meta:
        model = Signatory
        fields = ('name', 'email', 'url', 'location')

    def save(self, commit=True):
        try:
            return Signatory.objects.get(email=self.instance.email)
        except Signatory.DoesNotExist:
            pass

        return super(SignupForm, self).save(commit)
