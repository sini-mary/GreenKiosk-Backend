from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    email = models.CharField(max_length=32)
    address = models.TextField()
    
    def __str__(self):
        return f" {self.first_name}  {self.last_name}"
