 #! Vehicle Serializers
from pyexpat import model
from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        #! fields must match what is in db.
        fields = ['id', 'vin', 'year', 'make', 'model', 'trim', 'engine_size', 'transmission_type', 'drive_type', 'fuel_type','user_id' ]