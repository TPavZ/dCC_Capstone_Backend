 #! Service Serializers
from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        #! fields must match what is in db.
        fields = ['id', 'name', 'phone_number', 'website', 'street', 'city', 'state', 'zipcode', 'contact_first_name', 'contact_last_name', 'details']