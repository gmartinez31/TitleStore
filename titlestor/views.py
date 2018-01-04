from django.template.response import TemplateResponse
from django.http import Http404
from .forms import ClientForm, VehicleForm


def index(request):
    Cform = ClientForm()
    Vform = VehicleForm()

    return TemplateResponse(request, 'index.html', {'Cform': Cform, 'Vform': Vform})

def about(request):
    return TemplateResponse(request, 'about.html', {})

def confirmation(request):
    return TemplateResponse(request, 'confirmation.html', {})

def error(request):
    return TemplateResponse(request, 'error.html', {})

