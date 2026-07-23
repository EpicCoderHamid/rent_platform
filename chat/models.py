from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ChatRoom(models.Model):
    """Chat room between two users"""
    participants = models.ManyToManyField(User, related_name='chat_rooms')
    listing = models.ForeignKey('listings.Listing', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at']
    
    def __str__(self):
        return f"Chat: {', '.join([u.username for u in self.participants.all()])}"
    
    def get_other_user(self, user):
        """Get the other participant in the chat"""
        return self.participants.exclude(id=user.id).first()
    
    def get_unread_count(self, user):
        """Get unread messages count for a user"""
        return self.messages.filter(is_read=False).exclude(sender=user).count()

class Message(models.Model):
    """Individual message with status tracking"""
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    message = models.TextField()
    image = models.ImageField(upload_to='chat_images/', null=True, blank=True)
    
    # Message Status Fields
    is_sent = models.BooleanField(default=True)  # Sent to server
    is_delivered = models.BooleanField(default=False)  # Delivered to receiver's device
    is_read = models.BooleanField(default=False)  # Receiver has seen
    read_at = models.DateTimeField(null=True, blank=True)  # When message was read
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"{self.sender.username}: {self.message[:50]}"
    
    def mark_as_delivered(self):
        """Mark message as delivered"""
        if not self.is_delivered:
            self.is_delivered = True
            self.save(update_fields=['is_delivered'])
    
    def mark_as_read(self):
        """Mark message as read"""
        if not self.is_read:
            self.is_read = True
            self.read_at = timezone.now()
            self.save(update_fields=['is_read', 'read_at'])
    
    @property
    def status_icon(self):
        """Return status icon HTML based on message status"""
        if self.is_read:
            return '<i class="fas fa-check-double text-primary" title="Read"></i>'
        elif self.is_delivered:
            return '<i class="fas fa-check-double text-secondary" title="Delivered"></i>'
        else:
            return '<i class="fas fa-check text-secondary" title="Sent"></i>'
    
    @property
    def status_text(self):
        """Return status text"""
        if self.is_read:
            return "Read"
        elif self.is_delivered:
            return "Delivered"
        else:
            return "Sent"