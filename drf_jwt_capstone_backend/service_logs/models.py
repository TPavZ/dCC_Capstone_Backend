from django.db import models
from django.contrib.auth import get_user_model  
User=get_user_model()
# Create your models here.
class Service(models.Model):
    user = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    vehicle = models.ForeignKey('vehicles.Vehicle', null=True, blank=True, on_delete=models.SET_NULL) #TODO Somehow be able to connect to the users vehicle.
    shop = models.ForeignKey('shops.Shop', null=True, blank=True, on_delete=models.SET_NULL) #TODO Somehow be able to connect to the shop work was done at.
    service_date = models.DateField(auto_now=True)
    service_grand_total = models.DecimalField(max_digits=7, default=0.0, decimal_places=2)

    details = models.TextField(blank=True, null=True)
