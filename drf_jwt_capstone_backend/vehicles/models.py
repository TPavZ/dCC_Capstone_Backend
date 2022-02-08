from django.db import models
from django.contrib.auth import get_user_model   
User=get_user_model()
# Create your models here.

class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vin = models.CharField(max_length=17)
    year = models.IntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    trim = models.CharField(max_length=100)
    engine_size = models.IntegerField()
    transmission_type = models.CharField(max_length=50)
    drive_type = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    

