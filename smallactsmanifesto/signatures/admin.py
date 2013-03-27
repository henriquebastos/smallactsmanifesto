# coding: utf-8
from django.contrib import admin
from .models import Signatory


class SignatoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'url', 'location', 'signed_at', 'is_active')
    date_hierarchy = 'signed_at'
    search_fields = ('name', 'email', 'url', 'location', 'signed_at')
    list_filter = ['signed_at', 'is_active']


admin.site.register(Signatory, SignatoryAdmin)
