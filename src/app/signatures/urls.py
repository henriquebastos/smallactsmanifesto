from django.conf import settings
from django.conf.urls.defaults import *
from app.shortcuts import route


urlpatterns = patterns('app.signatures.views',
    route(r'^signup/$', GET='new', POST='create', name='signup'),
    url(r'^$', 'index', name='signatures-list'),
    url(r'^signup/confirm_email/(\w+)/$', 'confirm_email', name='confirm_email'),
)

#if settings.DEBUG:
#    urlpatterns += patterns('django.views.generic.simple',
#        (r'^signed/$', 'direct_to_template', {'template': 'signatures/signed.html'},
#            {'MEDIA_URL': settings.MEDIA_URL}),
#    )