# coding: UTF-8
import hashlib
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse as r
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .utils import mark_safe_lazy as safe


HELP_NAME = safe(_('Your name to be shown on the signatories list.'))
HELP_EMAIL = safe(_('Your email is important so we can send you a confirmation email.'
                    '<br />Your email will not be published or used in any other way.'))
HELP_URL = safe(_('<em>This field is optional.</em> An url that will be linked '
                  'to you name on the signatories list.'))
HELP_LOCATION = safe(_('<em>This field is optional.</em> Where are you from?'))


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
        return "%s - %s" % (self.name, self.email)

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
        return u"http://%s%s" % (site.domain, path)
