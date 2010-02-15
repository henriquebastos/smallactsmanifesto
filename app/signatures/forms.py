# encoding: utf-8
from django import forms

from models import Signatory


class SignatoryForm(forms.ModelForm):
    class Meta:
        model = Signatory
        exclude = ('signed_at', 'is_active', 'confirmation_key')
