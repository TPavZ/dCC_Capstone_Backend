 #! Shop URL
from django.urls import path
from . import views

urlpatterns = [
    path('all/shops', views.get_all_shops),
]