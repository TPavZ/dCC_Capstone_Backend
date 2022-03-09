#! Shop Serializers
from rest_framework import serializers
from .models import Shop
from django.contrib.auth.models import User


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        #! fields must match what is in db.
        fields = ['id', 'name', 'phone_number', 'website', 'street', 'city',
                  'state', 'zipcode', 'contact_first_name', 'contact_last_name', 'details']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
