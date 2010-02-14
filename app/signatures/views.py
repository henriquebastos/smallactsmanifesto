from django.http import HttpResponse

def new(request):
    return HttpResponse("New")

def create(request):
    return HttpResponse("Create")