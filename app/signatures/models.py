# -*- coding UTF-8 -*-
from django.db import models


class Signatory(models.Model):
    """
    Manifesto's signatory
    """
    name = models.CharField("Name", max_length=200)
    email = models.EmailField("E-mail", unique=True)
    url = models.URLField("Url", blank=True)
    location = models.CharField("Location", max_length=200)
    signed_at = models.DateTimeField("Signed At", auto_now_add=True)

    def __unicode__(self):
        return "%s - %s" % (self.name, self.email)

