from django.db import models

# if you make changes or add something be sure to run migrations: p man.py makemigrations then migrate

class Clients(models.Model):
    firstName = models.CharField(max_length=256)
    middleName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)
    phone = models.IntegerField()
    email = models.EmailField()
    dlNum = models.IntegerField()
    expDate = models.IntegerField()
    vehicle = models.ForeignKey(
        'Vehicles',
        on_delete=models.CASCADE,
        # stuff
    )

class Vehicles(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    color = models.CharField(max_length=256)
    odometer = models.IntegerField()
    lpNum = models.IntegerField()
    vin = models.IntegerField()
    client = models.ForeignKey(
        'Clients',
        on_delete=models.CASCADE,
        # stuff
    )
