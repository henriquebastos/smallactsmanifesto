# coding: utf-8
from django.conf.urls import patterns, include, url
from .views import SignupView, ConfirmView, SignupSuccessView


urlpatterns = patterns('smallactsmanifesto.signatures.views',
    url(r'^$', SignupView.as_view(), name='signup'),
    url(r'^success/$', SignupSuccessView.as_view(), name='success'),
    url(r'^confirm/(?P<slug>\w+)/$', ConfirmView.as_view(), name='confirm'),
)
