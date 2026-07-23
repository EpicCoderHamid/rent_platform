# locations/models.py - Without GIS
from django.db import models
from django.contrib.auth.models import User

class Province(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='cities')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    # location = PointField - REMOVE THIS LINE
    
    def __str__(self):
        return f"{self.name}, {self.province.name}"

class UserLocation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='location')
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    # location = PointField - REMOVE THIS LINE
    use_live_location = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)