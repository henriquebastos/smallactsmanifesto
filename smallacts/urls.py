from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^signup/', include('smallacts.signatures.urls', namespace='signatures')),
    url(r'^', include('smallacts.core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
)
