    #! Vehicle Views
    # TODO for production change authetications back.
#from django.http.response import Http404
#from django.shortcuts import render
from rest_framework import status
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from .models import Vehicle
from .serializers import VehicleSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_vehicles(request):
    vehicles = Vehicle.objects.all()
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])  # !IsAuthenticated
def get_user(request, user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_vehicles(request, user_id):
    if request.method == 'POST':
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        vehicles = Vehicle.objects.filter(user_id = request.user.id)
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([AllowAny])  # !IsAuthenticated
def update_vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    serializer = VehicleSerializer(vehicle, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([AllowAny])  # !IsAuthenticated
def delete_vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    if request.user.id == vehicle.user.id:
        serializer = VehicleSerializer(vehicle, many=False)
        vehicle.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)