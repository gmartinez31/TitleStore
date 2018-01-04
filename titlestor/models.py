from django.db import models

# if you make changes or add something be sure to run migrations: p man.py makemigrations then migrate

class Client(models.Model):
    firstName = models.CharField(max_length=256)
    middleName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    dlNum = models.CharField(max_length=16)
    expDate = models.DateField()
    vehicle = models.ForeignKey(
        'Vehicle',
        on_delete=models.CASCADE,
        # stuff
    )

    def __str__(self):
        return self.firstName + self.lastName

class Vehicle(models.Model):
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=256, default='Make')
    model = models.CharField(max_length=256, default='Model')
    color = models.CharField(max_length=256, default='Color')
    odometer = models.CharField(max_length=6)
    lpNum = models.CharField(max_length=7)
    vin = models.CharField(max_length=17)

    def __str__(self):
        return self.year + self.make + self.model