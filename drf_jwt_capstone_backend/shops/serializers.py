 #! Shop Serializers
from rest_framework import serializers
from .models import Shop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        #! fields must match what is in db.
        fields = ['id', 'name', 'phone_number', 'website', 'street', 'city', 'zipcode', 'contact_first_name', 'contact_last_name', 'details']