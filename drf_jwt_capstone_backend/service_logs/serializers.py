 #! Service Serializers
from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        #! fields must match what is in db.
        fields = ['id', 'battery_service', 'brakefluid_service', 'brakefront_service', 'brakerear_service', 'bulb_replacement', 'cabinfilter_replacement', 'coolant_service', 'differential_service', 'drivebelt_replacement', 'electrical_investigation',  'enginefilter_replacement', 'exahust_service', 'fuelfilter_replacement', 'major_repair', 'mechanical_investigation', 'oil_change', 'powersteering_service', 'sparkplug_service', 'steering_repair', 'suspension_repair', 'tire_replacement', 'tire_rotation', 'transfercase_service', 'transmission_service', 'wiperblade_replacement', 'other_services']