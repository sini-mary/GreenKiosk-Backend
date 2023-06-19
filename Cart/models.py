from django.db import models

# Create your models here.
class Cart(models.Model):
    product =models.TextField()
    total = models.IntegerField()
    number_of_products = models.IntegerField()
    shipping_cost = models.FloatField()
    Payment_options = models.TextField()
    discounts = models.FloatField()
    
    def __str__(self):
        return  self.product
