 #! Vehicle URL
from django.urls import path
from . import views

urlpatterns = [
    path('', views.VehicleList.as_view())
]