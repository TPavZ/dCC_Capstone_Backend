    #! Service Views
    # TODO for production change authetications back.
#from django.http.response import Http404
#from django.shortcuts import render
from rest_framework import status
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Service
from .serializers import ServiceSerializer
from .serializers import CreateServiceSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])  # !IsAuthenticated
def get_user(request, user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([AllowAny])  # !IsAuthenticated
def user_services(request):
    if request.method == 'POST':
        serializer = CreateServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        Services = Service.objects.filter(user_id = request.user.id)
        serializer = ServiceSerializer(Services, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([AllowAny])  # !IsAuthenticated
def update_service(request, service_id):
    service = Service.objects.get(id=service_id)
    serializer = ServiceSerializer(service, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([AllowAny])  # !IsAuthenticated
def delete_service(request, service_id):
    service = Service.objects.get(id=service_id)
    if request.user.id == Service.user.id:
        serializer = ServiceSerializer(service, many=False)
        Service.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


""" from django.http.response import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Service
from .serializers import ServiceSerializer
from django.contrib.auth import get_user_model   
User=get_user_model() """


""" class ServiceList(APIView):

    permission_classes = [AllowAny] #! Change later
    
    def get(self, request):
        service = Service.objects.all()
        serializer = ServiceSerializer(service, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShopDetails(APIView):

    permission_classes = [AllowAny] #! Change later

    def get_object(self, pk):
        try:
            return Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            raise Http404            

    def get(self, request, pk):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)
        
    def put(self, request, pk):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        service = self.get_object(pk)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) """
