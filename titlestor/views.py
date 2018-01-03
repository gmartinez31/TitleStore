from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def confirmation(request):
    return render(request, 'confirmation.html')

def error(request):
    return render(request, 'error.html')