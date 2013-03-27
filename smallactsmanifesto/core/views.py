# coding: utf-8
from django.views.generic.simple import direct_to_template
from smallacts.signatures.models import Signatory


def index(request):
    return direct_to_template(request, 'index.html', {
        'signatories' : Signatory.objects.all(),
    })


def community_badges(request):
    badges = (
        dict(size='80x15',  name='light default', sufix='80x15'),
        dict(size='80x15',  name='dark blue',     sufix='80x15-blue'),
        dict(size='88x31',  name='light default', sufix='88x31'),
        dict(size='88x31',  name='dark blue',     sufix='88x31-blue'),
        dict(size='110x32', name='light default', sufix='110x32'),
        dict(size='110x32', name='dark blue',     sufix='110x32-blue'),
        dict(size='120x60', name='light default', sufix='120x60'),
        dict(size='120x60', name='dark blue',     sufix='120x60-blue'),
    )
    return direct_to_template(request, 'community-badges.html',
                              {'badges': badges})
