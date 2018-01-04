from django.contrib import admin
from .models import Client, Vehicle

# admin username and password (for now) is: titlestor
admin.site.register(Client)
admin.site.register(Vehicle)