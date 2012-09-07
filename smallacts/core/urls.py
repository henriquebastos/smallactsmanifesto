# coding: utf-8
from django.conf.urls import patterns, include, url


urlpatterns = patterns('smallacts.core.views',
    url(r'^$', 'index', name='index'),
    url(r'^community-badges/$', 'community_badges', name='community-badges'),
)
