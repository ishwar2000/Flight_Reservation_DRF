from django.db import models

# Create your models here.

class flightModel(models.Model):
    flightNumber = models.CharField(max_legnth =10)
    operatingAirline = models.CharField(max_legnth =20)
    DepartureCity = models.CharField(max_legnth =20)
    arrivalCity = models.CharField(max_legnth =20)
    dateOfDeparture = models.TimeField()
    
class passengerModel(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    mob = models.CharField(max_length=13)


class reservation(models.Model):
    