    #! Vehicle Serializers
from pyexpat import model
from rest_framework import serializers
from .models import Vehicle
from django.contrib.auth.models import User


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        #! fields must match what is in db.
        fields = ['id', 'service_cost', 'vin', 'year', 'make', 'model', 'trim', 'engine_size',
                  'transmission_type', 'drive_type', 'fuel_type', 'user_id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
