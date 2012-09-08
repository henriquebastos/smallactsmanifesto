# coding: utf-8
from django.conf.urls import patterns, include, url


urlpatterns = patterns('smallacts.signatures.views',
    url(r'^$', 'signup', name='signup'),
)
