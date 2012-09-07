# coding: utf-8
from django.conf.urls import patterns, include, url


urlpatterns = patterns('smallacts.core.views',
   url(r'^$', 'index', name='index'),
)
