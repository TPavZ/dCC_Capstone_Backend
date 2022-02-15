    #! Vehicle URL
from django.urls import path
from . import views

urlpatterns = [
    path('addvehicle/', views.user_vehicles),
]
