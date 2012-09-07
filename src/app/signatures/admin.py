# -*- coding: utf-8 -*-
from django.contrib import admin

import models


admin.site.register(models.Signatory, admin.ModelAdmin)
