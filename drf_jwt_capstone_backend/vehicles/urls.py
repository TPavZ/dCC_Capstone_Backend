    #! Vehicle URL
from django.urls import path
from . import views

urlpatterns = [
    path('allvehicles/', views.get_all_vehicles),
    path('<int:user_id>/', views.user_vehicles),
    path('delete/<int:vehicle_id>/', views.delete_vehicle),
    path('edit/<int:vehicle_id>/', views.update_vehicle),
    path('user/<int:user_id>/', views.get_user)
]
