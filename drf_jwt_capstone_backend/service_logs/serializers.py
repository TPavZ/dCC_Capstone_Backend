#! Service Serializers
from rest_framework import serializers
from vehicles.models import Vehicle
from .models import Service
from django.contrib.auth.models import User


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        #! fields must match what is in db.
        fields = ["id", "user_id", "vehicle_id", "service_grand_total", "current_mileage", "service_date", "battery_service", "brakefluid_service", "brakefront_service", "brakerear_service", "bulb_replacement", "cabinfilter_replacement", "coolant_service", "differential_service", "drivebelt_replacement", "electrical_investigation",  "enginefilter_replacement", "exahust_service",
                  "fuelfilter_replacement", "mechanical_investigation", "oil_change", "powersteering_service", "sparkplug_service", "steering_repair", "suspension_repair", "tire_repair", "tire_replacement", "tire_rotation", "transfercase_service", "transmission_service", "wiperblade_replacement", "major_repairs", "other_services", "service_details"]


class CreateServiceSerializer(serializers.ModelSerializer):
    vehicle = serializers.PrimaryKeyRelatedField(
        queryset=Vehicle.objects.all())
    class Meta:
        model = Service
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]
