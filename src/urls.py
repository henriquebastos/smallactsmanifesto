from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # signatures
    (r'^', include('app.signatures.urls')),
)

# BADGES
badges = (
    { 'size': '80x15', 'name': 'light default', 'sufix': '80x15' },
    { 'size': '80x15', 'name': 'dark blue', 'sufix': '80x15-blue' },
    { 'size': '88x31', 'name': 'light default', 'sufix': '88x31' },
    { 'size': '88x31', 'name': 'dark blue', 'sufix': '88x31-blue' },
    { 'size': '110x32', 'name': 'light default', 'sufix': '110x32' },
    { 'size': '110x32', 'name': 'dark blue', 'sufix': '110x32-blue' },
    { 'size': '120x60', 'name': 'light default', 'sufix': '120x60' },
    { 'size': '120x60', 'name': 'dark blue', 'sufix': '120x60-blue' },
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^community-badges/$', 'direct_to_template',
        {
            'template': 'community-badges.html',
            'extra_context': { 'badges': badges },
        }
    ),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
