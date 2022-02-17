    #! Service URL
from django.urls import path
from . import views

urlpatterns = [
    path('allservices/', views.get_all_services),
    path('addservice/', views.user_services),
    path('user/services/', views.user_services),
    path('user/vehicle/services/<int:vehicle_id>/', views.get_all_services_pervehicle),
]
