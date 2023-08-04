from django.db import models
from Order.models import Order

# Create your models here.
class Shipment(models.Model):
    orderrs = models.ManyToManyField(Order)
    date = models.DateField()
    order = models.TextField()
    location = models.TextField()
    type_of_delivery = models.BooleanField()
    shipment_cost = models.FloatField()
    status = models.TextField()
    delivery_time = models.TimeField()
    
    def __str__(self) :
        return self.location