from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.conf import settings

from models import Signatory
from forms import SignatoryForm

def new(request):
    form = SignatoryForm()
    return render_to_response('signatures/form.html', {'form': form})

def create(request):
    form = SignatoryForm(request.POST)
    try:
        form.save()
    except ValueError:
        return render_to_response('signatures/form.html', {'form': form})
    return render_to_response('signatures/signed.html')

def index(request):
    signatures = Signatory.objects.filter(is_active=True)
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'signatures': signatures
    }
    return render_to_response('signatures/list.html', context)
