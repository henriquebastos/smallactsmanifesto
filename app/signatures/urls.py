from django.conf import settings
from django.conf.urls.defaults import *
from shortcuts import route
from views import new, create


urlpatterns = patterns('',
    route(r'^signup/', GET=new, POST=create, name="signup")
)
