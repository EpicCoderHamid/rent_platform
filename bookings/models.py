# bookings/models.py
from django.db import models
from django.contrib.auth.models import User
from listings.models import Listing
from datetime import date, datetime

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        # Calculate total price only if both dates are date objects
        if self.start_date and self.end_date:
            # Ensure they are date objects
            if isinstance(self.start_date, str):
                from datetime import datetime
                self.start_date = datetime.strptime(self.start_date, '%Y-%m-%d').date()
            if isinstance(self.end_date, str):
                from datetime import datetime
                self.end_date = datetime.strptime(self.end_date, '%Y-%m-%d').date()
            
            # Calculate days
            days = (self.end_date - self.start_date).days
            if days < 0:
                days = 0  # Invalid dates
            self.total_price = days * self.listing.price_per_day
        else:
            self.total_price = 0
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.user.username} - {self.listing.title}'