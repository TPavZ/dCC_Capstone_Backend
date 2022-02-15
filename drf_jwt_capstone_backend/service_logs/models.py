from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Service(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    # TODO Somehow be able to connect to the users vehicle.
    vehicle = models.ForeignKey('vehicles.Vehicle', null=True, blank=True, on_delete=models.SET_NULL)
    current_mileage = models.IntegerField()
    # TODO Somehow be able to connect to the shop work was done at.
    shop = models.ForeignKey('shops.Shop', null=True, blank=True, on_delete=models.SET_NULL)
    service_date = models.DateField()
    service_grand_total = models.DecimalField(max_digits=7, default=0.0, decimal_places=2)
    battery_service = models.BooleanField(null=True, blank=True)
    brakefluid_service = models.BooleanField(null=True, blank=True)
    brakefront_service = models.BooleanField(null=True, blank=True)
    brakerear_service = models.BooleanField(null=True, blank=True)
    bulb_replacement = models.BooleanField(null=True, blank=True)
    cabinfilter_replacement = models.BooleanField(null=True, blank=True)
    coolant_service = models.BooleanField(null=True, blank=True)
    differential_service = models.BooleanField(null=True, blank=True)
    drivebelt_replacement = models.BooleanField(null=True, blank=True)
    electrical_investigation = models.BooleanField(null=True, blank=True)
    enginefilter_replacement = models.BooleanField(null=True, blank=True)
    exahust_service = models.BooleanField(null=True, blank=True)
    fuelfilter_replacement = models.BooleanField(null=True, blank=True)
    mechanical_investigation = models.BooleanField(null=True, blank=True)
    oil_change = models.BooleanField(null=True, blank=True)
    powersteering_service = models.BooleanField(null=True, blank=True)
    sparkplug_service = models.BooleanField(null=True, blank=True)
    steering_repair = models.BooleanField(null=True, blank=True)
    suspension_repair = models.BooleanField(null=True, blank=True)
    tire_repair = models.BooleanField(null=True, blank=True)
    tire_replacement = models.BooleanField(null=True, blank=True)
    tire_rotation = models.BooleanField(null=True, blank=True)
    transfercase_service = models.BooleanField(null=True, blank=True)
    transmission_service = models.BooleanField(null=True, blank=True)
    wiperblade_replacement = models.BooleanField(null=True, blank=True)
    major_repairs = models.TextField(null=True, blank=True)
    other_services = models.TextField(blank=True, null=True)
    service_details = models.TextField(blank=True, null=True)
