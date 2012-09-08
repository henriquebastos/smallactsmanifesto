# coding: utf-8
from django import forms
from .models import Signatory


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signatory
        fields = ('name', 'email', 'url', 'location')

    def save_if_new(self):
        self.full_clean()
        # verify if signatory has already submited this form.
        q = Signatory.objects.filter(email=self.data['email'])
        if q:
            instance = q.get()
        else:
            instance = self.save()
        return instance
