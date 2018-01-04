from django.db import models

# if you make changes or add something be sure to run migrations: p man.py makemigrations then migrate

class Clients(models.Model):
    firstName = models.CharField(max_length=256, default='First')
    middleName = models.CharField(max_length=256, default='Middle')
    lastName = models.CharField(max_length=256, default='Last')
    phone = models.IntegerField()
    email = models.EmailField()
    dlNum = models.IntegerField()
    expDate = models.IntegerField()
    vehicle = models.ForeignKey(
        'Vehicles',
        on_delete=models.CASCADE,
        # stuff
    )

    def __str__(self):
        return self.firstName + self.lastName

class Vehicles(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=256, default='Make')
    model = models.CharField(max_length=256, default='Model')
    color = models.CharField(max_length=256, default='Color')
    odometer = models.IntegerField()
    lpNum = models.IntegerField()
    vin = models.IntegerField()

    def __str__(self):
        return self.year + self.make + self.model