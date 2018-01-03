from django.template.response import TemplateResponse

def index(request):
    return TemplateResponse(request, 'index.html', {})

def about(request):
    return TemplateResponse(request, 'about.html', {})

def confirmation(request):
    return TemplateResponse(request, 'confirmation.html', {})

def error(request):
    return TemplateResponse(request, 'error.html', {})