from django.http import Http404
from django.views.generic.simple import direct_to_template, redirect_to
from django.core.urlresolvers import reverse
from django.conf import settings

from models import Signatory
from forms import SignatoryForm
from utils import send_email_confirmation


def new(request):
    form = SignatoryForm()
    context = {
        'form': form
    }
    return direct_to_template(request, 'signatures/form.html', context)


def create(request):
    form = SignatoryForm(request.POST)

    context = {
        'form': form
    }

    try:
        signatory = form.save_if_new()
        send_email_confirmation(signatory)
    except ValueError:
        return direct_to_template(request, 'signatures/form.html', context)

    return direct_to_template(request, 'signatures/signed.html', context)


def index(request):
    signatures = Signatory.objects.filter(is_active=True)
    context = {
        'signatures': signatures
    }
    return direct_to_template(request, 'signatures/list.html', context)


def confirm_email(request, confirmation_key):
    try:
        signatory = Signatory.objects.get(confirmation_key=confirmation_key)
        signatory.is_active = True
        signatory.save()
    except Signatory.DoesNotExist:
        raise Http404

    context = {
        'signatory': signatory,
    }
    return direct_to_template(request, 'signatures/confirmed.html', context)

