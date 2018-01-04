from django import forms
from .models import Client, Vehicle

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('vehicle', )


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
