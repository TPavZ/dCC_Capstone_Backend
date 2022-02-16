    #! Shop URL
from django.urls import path
from . import views

urlpatterns = [
    path('allshops/', views.get_all_shops),
]
