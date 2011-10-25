# encoding: utf-8
from django import forms

from models import Signatory


class SignatoryForm(forms.ModelForm):
    class Meta:
        model = Signatory
        exclude = ('signed_at', 'is_active', 'confirmation_key')

    def save_if_new(self):
        self.full_clean()
        # verify if signatory has already submited this form.    
        q = Signatory.objects.filter(email=self.data['email'])
        if q:
            instance = q.get()
        else:
            instance = self.save()
        return instance
