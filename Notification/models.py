from django.db import models

# Create your models here.
class Notification(models.Model):
    message = models.TextField()
    time = models.DateTimeField()
    customer = models.TextField()
    types = models.BooleanField()
    
    def __str__(self):
        return self.message

