from django import forms
from .models import Client, Vehicle
from django.utils.translation import gettext_lazy as _

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('vehicle', )
        labels = {
            'firstName': _('First Name'),
            'middleName': _('Middle Name'),
            'lastName': _('Last Name'),
            'phone': _('Phone Number'),
            'email': _('Email Address'),
            'dlNum': _('Driver"s License Number'),
            'expDate': _('DL Expiration Date')
        }
        widgets = {
            
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        labels = {
            'year': _('Vehicle Year'),
            'make': _('Vehicle Make'),
            'model': _('Vehicle Model'),
            'color': _('Vehicle Color'),
            'odometer': _('Odometer'),
            'lpNum': _('License Plate Number'),
            'vin': _('VIN Number')
        }
