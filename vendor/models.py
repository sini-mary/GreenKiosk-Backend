from django.db import models

# Create your models here.
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=32)
    location = models.TextField()
    contact = models.IntegerField()
    store_name = models.CharField(max_length = 32)
    password = models.CharField(max_length = 32)
    username = models.CharField(max_length = 32)