from django.db import models

# Create your models here.
class Hotel(models.Model):
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    service_type = models.CharField(max_length=120)
    address = models.TextField(null=True)
    postal_code = models.CharField(max_length=8, null=True, blank=True)
    price = models.CharField(max_length=8,null=True)
    rating = models.CharField(max_length=2)

    
