# coding: utf-8
from django.contrib import admin
from django.utils.translation import ungettext
from .models import Signatory


class SignatoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'url', 'location', 'signed_at', 'is_active')
    date_hierarchy = 'signed_at'
    search_fields = ('name', 'email', 'url', 'location', 'signed_at')
    list_filter = ['signed_at', 'is_active']

    actions = ['activate']

    def activate(self, request, qs):
        count = qs.update(is_active=True)

        msg = ungettext(
            '%d signature was activated.',
            '%d signatures were activated.',
            count
        )

        self.message_user(request, msg % count)


admin.site.register(Signatory, SignatoryAdmin)
