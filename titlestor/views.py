from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello, world")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('about')