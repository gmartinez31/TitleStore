from django.template.response import TemplateResponse
from django.http import Http404
from .forms import IndexForm

def index(request):
    return TemplateResponse(request, 'index.html', {})
    
    def get(self, request):
        form = IndexForm()
        return TemplateResponse(request, 'index.html', { 'form': form })

def about(request):
    return TemplateResponse(request, 'about.html', {})

def confirmation(request):
    return TemplateResponse(request, 'confirmation.html', {})

def error(request):
    return TemplateResponse(request, 'error.html', {})

