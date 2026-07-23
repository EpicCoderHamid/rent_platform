# users/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=100, blank=True)
    is_seller = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profiles/', default='default.jpg')
    CNIC = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cnic_front = models.ImageField(upload_to='cnic_images/', blank=True, null=True)
    cnic_back = models.ImageField(upload_to='cnic_images/', blank=True, null=True)
    cnic_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username}\'s Profile'

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)