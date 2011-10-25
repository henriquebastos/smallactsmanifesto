from django.http import Http404
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.conf import settings

from models import Signatory
from forms import SignatoryForm
from utils import send_email_confirmation


def new(request):
    form = SignatoryForm()
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'form': form
    }
    return render_to_response('signatures/form.html', context)

def create(request):
    form = SignatoryForm(request.POST)
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'form': form
    }
    try:
        signatory = form.save_if_new()
        send_email_confirmation(signatory)
    except ValueError:
        return render_to_response('signatures/form.html', context)
    return render_to_response('signatures/signed.html', context)

def index(request):
    signatures = Signatory.objects.filter(is_active=True)
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'signatures': signatures
    }
    return render_to_response('signatures/list.html', context)

def confirm_email(request, confirmation_key):
    try:
        signatory = Signatory.objects.get(confirmation_key=confirmation_key)
        signatory.is_active = True
        signatory.save()
    except Signatory.DoesNotExist:
        raise Http404

    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'signatory': signatory,
    }
    return render_to_response('signatures/confirmed.html', context)

