# coding: utf-8
from django import forms
from .models import Signatory


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signatory
        fields = ('name', 'email', 'url', 'location')

    def save(self, commit=True):
        try:
            return Signatory.objects.get(email=self.instance.email)
        except Signatory.DoesNotExist:
            pass

        return super(SignupForm, self).save(commit)
