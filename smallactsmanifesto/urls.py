from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^signup/', include('smallactsmanifesto.signatures.urls', namespace='signatures')),
    url(r'^', include('smallactsmanifesto.core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
)
