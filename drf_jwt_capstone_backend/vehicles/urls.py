 #! Vehicle URL
from django.urls import path
from . import views

urlpatterns = [
    path('all/vehicles', views.get_all_vehicles),
]