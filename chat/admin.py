# chat/admin.py
from django.contrib import admin
from .models import ChatRoom, Message

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_participants', 'listing', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['participants__username', 'listing__title']
    filter_horizontal = ['participants']
    
    def get_participants(self, obj):
        return ", ".join([user.username for user in obj.participants.all()])
    get_participants.short_description = 'Participants'

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'chat_room', 'message_preview', 'is_sent', 'is_delivered', 'is_read', 'created_at']
    list_filter = ['is_sent', 'is_delivered', 'is_read', 'created_at']
    search_fields = ['sender__username', 'message']
    readonly_fields = ['is_sent', 'is_delivered', 'is_read', 'read_at']
    
    def message_preview(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    message_preview.short_description = 'Message'