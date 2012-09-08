# coding: UTF-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .utils import generate_confirmation_key


class Signatory(models.Model):
    "Manifesto's signatory"

    name = models.CharField(_('Name'), max_length=200)
    email = models.EmailField(_('E-mail'), unique=True)
    url = models.URLField(_('Url'), blank=True)
    location = models.CharField(_('Location'), max_length=200, blank=True)

    signed_at = models.DateTimeField(_('Signed At'), auto_now_add=True)
    is_active = models.BooleanField(_('Is active?'), default=False)

    confirmation_key = models.CharField(_('Confirmation Key'), max_length=40)

    class Meta:
        ordering = ['name', 'signed_at']

    def __unicode__(self):
        return "%s - %s" % (self.name, self.email)

    def save(self, *args, **kwargs):
        # create a confirmation_key
        if not self.confirmation_key:
            self.confirmation_key = generate_confirmation_key(self.email)

        return super(Signatory, self).save(*args, **kwargs)
