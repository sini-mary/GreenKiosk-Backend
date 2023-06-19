from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length= 32)
    order_number = models.IntegerField()
    total = models.FloatField()
    date = models.DateField()
    payment_options = models.CharField( max_length = 32)
    
    def __str__(self) :
        return  self.name
    
