from django.conf import settings
from django.conf.urls.defaults import *
from shortcuts import route
from views import new, create, index


urlpatterns = patterns('',
    route(r'^signup/', GET=new, POST=create, name="signup"),
    url(r'^$', index, name="signatures-list")
)
