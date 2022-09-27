# coding: UTF-8
import hashlib
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse as r
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .utils import mark_safe_lazy as safe


HELP_NAME = safe(_('Your name to be shown on the signatories list.'))
HELP_EMAIL = safe(_('We need it to send you a confirmation email.'
                    " <em>We'll not use it in any other way.</em>"))
HELP_URL = safe(_('This will be linked to you name on the signatories list.'
                  ' <em>This field is optional.</em>'))
HELP_LOCATION = safe(_('Where are you from? <em>This field is optional.</em>'))


class Signatory(models.Model):
    """
    Manifesto's signatory
    """
    name = models.CharField(_('Name'), max_length=200, help_text=HELP_NAME)
    email = models.EmailField(_('E-mail'), help_text=HELP_EMAIL)
    url = models.URLField(_('Url'), blank=True, help_text=HELP_URL)
    location = models.CharField(_('Location'), max_length=200, blank=True, help_text=HELP_LOCATION)

    signed_at = models.DateTimeField(_('Signed At'), auto_now_add=True)
    is_active = models.BooleanField(_('Is active?'), default=False)

    confirmation_key = models.CharField(_('Confirmation Key'), max_length=40)

    class Meta:
        ordering = ['name', 'signed_at']

    def __unicode__(self):
        return f"{self.name} - {self.email}"

    def save(self, *args, **kwargs):
        # create a confirmation_key
        if not self.confirmation_key:
            self.confirmation_key = self._generate_confirmation_key()

        return super(Signatory, self).save(*args, **kwargs)

    def _generate_confirmation_key(self):
        return hashlib.sha1(self.email).hexdigest()

    def get_confirm_url(self):
        site = Site.objects.get_current()
        path = r('signatures:confirm', args=[self.confirmation_key])
        return f"http://{site.domain}{path}"
