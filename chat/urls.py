from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_list, name='chat-list'),
    path('room/<int:room_id>/', views.chat_room, name='chat-room'),
    path('start/<int:listing_id>/<int:seller_id>/', views.start_chat, name='start-chat'),
    path('send/<int:room_id>/', views.send_message, name='send-message'),
    path('get-messages/<int:room_id>/', views.get_messages, name='get-messages'),
    path('mark-read/<int:room_id>/', views.mark_messages_read, name='mark-messages-read'),
    path('unread-count/', views.get_unread_count, name='chat-unread-count'),
    path('message-status/<int:message_id>/', views.message_status_update, name='message-status'),
]
