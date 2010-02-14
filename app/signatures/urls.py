from django.conf import settings
from django.conf.urls.defaults import *
from shortcuts import route
from views import new, create


urlpatterns = patterns('',
    route(r'^signup/', GET=new, POST=create)
)

# / mostra o manifesto e a lista de signatarios em ordem alfabetica
# /signup get form signatures
# /signup post adiciona assinatura e redireciona pra /
# /signatures get lista assinatures
