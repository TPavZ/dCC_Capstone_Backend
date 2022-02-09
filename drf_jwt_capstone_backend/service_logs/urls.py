 #! Service URL
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServiceList.as_view())
]