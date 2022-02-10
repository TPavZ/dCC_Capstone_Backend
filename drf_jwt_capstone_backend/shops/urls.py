 #! Shop URL
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShopList.as_view()),
    path('shop/<int:pk>/', views.ShopDetails.as_view()),
]