from django.db import models
from inventory.models import Product
from  Order.models import Order
# Create your models here.
class Cart(models.Model):
    products = models.ManyToManyField(Product)
    orderrr =  models.OneToOneField(Order,on_delete=models.CASCADE,null=True)
    product =models.TextField()
    total = models.IntegerField()
    number_of_products = models.IntegerField()
    shipping_cost = models.FloatField()
    Payment_options = models.TextField()
    discounts = models.FloatField()
    
    
    def __str__(self):
        return  self.product
