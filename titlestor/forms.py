from django import forms
from .models import Client, Vehicle

class IndexForm(forms.Form):
    post = forms.CharField()