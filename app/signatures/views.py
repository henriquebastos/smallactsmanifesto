from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse

from forms import SignatoryForm

def new(request):
    form = SignatoryForm()
    return render_to_response('signatures/form.html', {'form': form})

def create(request):
    return HttpResponse("Create")