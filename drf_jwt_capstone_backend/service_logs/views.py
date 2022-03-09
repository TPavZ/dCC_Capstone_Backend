#! Service Views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Service
from vehicles.models import Vehicle
from .serializers import ServiceSerializer
from .serializers import CreateServiceSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from decimal import Decimal
User = get_user_model()

# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_services_pervehicle(request, vehicle_id):
    services = Service.objects.filter(vehicle_id=vehicle_id)
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request, user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_services(request):
    if request.method == 'POST':
        serializer = CreateServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)

            # update vehicle
            vehicleid = serializer.initial_data['vehicle']
            servicecost = Decimal(
                serializer.initial_data['service_grand_total'])
            vehicle = Vehicle.objects.get(id=vehicleid)
            vehicle.service_cost += servicecost
            vehicle.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        Services = Service.objects.filter(user_id=request.user.id)
        serializer = ServiceSerializer(Services, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_service(request, service_id):
    service = Service.objects.get(id=service_id)
    serializer = ServiceSerializer(service, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_service(request, service_id):
    service = Service.objects.get(id=service_id)
    vehicle = Vehicle.objects.get(id=service.vehicle_id)
    cost = Decimal(service.service_grand_total)
    if request.user.id == Service.user.id:
        serializer = ServiceSerializer(service, many=False)
        Service.delete()

        # updates vehicle
        vehicle.service_cost -= cost
        vehicle.save()

        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
