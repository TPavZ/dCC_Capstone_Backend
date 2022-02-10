 #! Service URL
from django.urls import path
from . import views

urlpatterns = [
    path('all/services', views.get_all_services)
]