from django.db import models


class Clients(models.Model):
    firstName = models.CharField()
    middleName = models.CharField()
    lastName = models.CharField()
    phone = models.IntegerField()
    email = models.CharField()
    dlNum = models.IntegerField()
    expDate = models.IntegerField()

class Vehicles(models.Model):
    year = models.IntegerField()
    make = models.CharField()
    model = models.CharField()
    color = models.CharField()
    odometer = models.IntegerField()
    lpNum = models.IntegerField()
    vin = models.IntegerField()
