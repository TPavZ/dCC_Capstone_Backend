    #! Vehicle URL
from django.urls import path
from . import views

urlpatterns = [
    path('addvehicle/', views.user_vehicles),
    path('allvehicles/', views.get_all_vehicles),
    path('<int:user_id>/', views.user_vehicles),
]
