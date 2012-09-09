# coding: utf-8
from django.conf.urls import patterns, include, url


urlpatterns = patterns('smallacts.signatures.views',
    url(r'^$', 'signup', name='signup'),
    url(r'^success/$', 'success', name='success'),
    url(r'^confirm/(?P<slug>\w+)/$', 'confirm', name='confirm'),
)
