from django.contrib import admin
from .models import Clients, Vehicles

# admin username and password (for now) is: titlestor
admin.site.register(Clients)
admin.site.register(Vehicles)