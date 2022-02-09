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
    trim = models.CharField(max_length=100, blank=True, null=True)
    #!
    ENGINE_CHOICES = (
        ('4 Cylinder', '4 Cylinder'),
        ('6 Cylinder','6 Cylinder'),
        ('8 Cylinder','8 Cylinder'),
        ('10 Cylinder','10 Cylinder'),
        ('12 Cylinder','12 Cylinder'),
        ('Other','Other'),
    )
    engine_size = models.CharField(max_length=50, choices=ENGINE_CHOICES, blank=True, null=True)
    #!
    TRANS_CHOICES = (
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
        ('CVT', 'CVT'),
    )
    transmission_type = models.CharField(max_length=50, null=True, blank=True,  choices=TRANS_CHOICES)
    #!
    DRIVE_CHOICES = (
        ('AWD', 'AWD'),
        ('4WD','4WD'),
        ('FWD','FWD'),
        ('RWD','RWD'),
    )
    drive_type = models.CharField(max_length=50, choices=DRIVE_CHOICES, blank=True, null=True)
    #!
    FUEL_CHOICES = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Other', 'Other'),
    )
    fuel_type = models.CharField(choices=FUEL_CHOICES, max_length=50, blank=True, null=True)
    

