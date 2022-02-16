    #! Shop Views
    # TODO for production change authetications back.
#from django.http.response import Http404
#from django.shortcuts import render
from rest_framework import status
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Shop
from .serializers import ShopSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_shops(request):
    shops = Shop.objects.all()
    serializer = ShopSerializer(shops, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])  # !IsAuthenticated
def get_user(request, user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([AllowAny])  # !IsAuthenticated
def user_shops(request):
    if request.method == 'POST':
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        shops= Shop.objects.filter(user_id = request.user.id)
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)
        


@api_view(['PUT'])
@permission_classes([AllowAny])  # !IsAuthenticated
def update_shop(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    serializer = ShopSerializer(shop, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([AllowAny])  # !IsAuthenticated
def delete_shop(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    if request.user.id == shop.user.id:
        serializer = ShopSerializer(shop, many=False)
        shop.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


""" class ShopList(APIView):

    permission_classes = [AllowAny] #! Change later
    
    def get(self, request):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShopDetails(APIView):

    permission_classes = [AllowAny] #! Change later

    def get_object(self, pk):
        try:
            return Shop.objects.get(pk=pk)
        except Shop.DoesNotExist:
            raise Http404            

    def get(self, request, pk):
        shop = self.get_object(pk)
        serializer = ShopSerializer(shop)
        return Response(serializer.data)
        
    def put(self, request, pk):
        shop = self.get_object(pk)
        serializer = ShopSerializer(shop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        shop = self.get_object(pk)
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) """
