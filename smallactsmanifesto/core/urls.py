# coding: utf-8
from django.conf.urls import patterns, include, url


urlpatterns = patterns('smallactsmanifesto.core.views',
    url(r'^$', 'index', name='index'),
    url(r'^community-badges/$', 'community_badges', name='community-badges'),
)
