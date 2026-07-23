from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.db.models import Q, OuterRef, Subquery
import json
from .models import ChatRoom, Message
from listings.models import Listing
from django.contrib.auth.models import User

@login_required
def chat_list(request):
    """List all chats for the current user"""
    chat_rooms = request.user.chat_rooms.all().prefetch_related('messages')
    
    # Add unread count to each chat room
    for room in chat_rooms:
        room.unread_count = room.get_unread_count(request.user)
        room.last_message = room.messages.last()
    
    context = {
        'chat_rooms': chat_rooms,
        'active_chats': True
    }
    return render(request, 'chat/chat_list.html', context)

@login_required
def chat_room(request, room_id):
    """View a specific chat room"""
    chat_room = get_object_or_404(ChatRoom, id=room_id, participants=request.user)
    other_user = chat_room.get_other_user(request.user)
    messages = chat_room.messages.all()
    
    # Mark unread messages as delivered when user opens chat
    unread_messages = messages.filter(is_read=False).exclude(sender=request.user)
    for msg in unread_messages:
        msg.mark_as_delivered()
    
    context = {
        'chat_room': chat_room,
        'other_user': other_user,
        'messages': messages,
        'listing': chat_room.listing
    }
    return render(request, 'chat/chat_room.html', context)

@login_required
def start_chat(request, listing_id, seller_id):
    """Start a new chat or get existing chat"""
    listing = get_object_or_404(Listing, id=listing_id)
    seller = get_object_or_404(User, id=seller_id)
    
    # Check if chat room already exists
    chat_room = ChatRoom.objects.filter(
        participants=request.user
    ).filter(
        participants=seller
    ).filter(
        listing=listing
    ).first()
    
    if not chat_room:
        chat_room = ChatRoom.objects.create(listing=listing)
        chat_room.participants.add(request.user, seller)
    
    return redirect('chat-room', room_id=chat_room.id)

@login_required
@require_POST
def send_message(request, room_id):
    """Send a new message"""
    chat_room = get_object_or_404(ChatRoom, id=room_id, participants=request.user)
    
    message_text = request.POST.get('message', '').strip()
    
    if message_text:
        message = Message.objects.create(
            chat_room=chat_room,
            sender=request.user,
            message=message_text,
            is_sent=True
        )
        
        # Return the message data with status
        return JsonResponse({
            'success': True,
            'message_id': message.id,
            'message': message.message,
            'created_at': message.created_at.strftime('%I:%M %p'),
            'status_icon': message.status_icon,
            'status_text': message.status_text
        })
    
    return JsonResponse({'success': False, 'error': 'Empty message'})

@login_required
def get_messages(request, room_id):
    """Get new messages (AJAX polling)"""
    chat_room = get_object_or_404(ChatRoom, id=room_id, participants=request.user)
    last_message_id = request.GET.get('last_id', 0)
    
    new_messages = chat_room.messages.filter(id__gt=last_message_id)
    
    messages_data = []
    for msg in new_messages:
        messages_data.append({
            'id': msg.id,
            'message': msg.message,
            'sender_id': msg.sender.id,
            'sender_username': msg.sender.username,
            'created_at': msg.created_at.strftime('%I:%M %p'),
            'is_sent': msg.is_sent,
            'is_delivered': msg.is_delivered,
            'is_read': msg.is_read,
            'status_icon': msg.status_icon,
            'status_text': msg.status_text
        })
        
        # Mark messages as delivered when receiver fetches them
        if msg.sender != request.user and not msg.is_delivered:
            msg.mark_as_delivered()
    
    return JsonResponse({'messages': messages_data, 'success': True})

@login_required
def mark_messages_read(request, room_id):
    """Mark all messages as read"""
    chat_room = get_object_or_404(ChatRoom, id=room_id, participants=request.user)
    
    # Mark all unread messages as read
    unread_messages = chat_room.messages.filter(is_read=False).exclude(sender=request.user)
    for msg in unread_messages:
        msg.mark_as_read()
    
    return JsonResponse({'success': True, 'marked_count': unread_messages.count()})

@login_required
def get_unread_count(request):
    """Get total unread messages count for current user"""
    total_unread = 0
    for room in request.user.chat_rooms.all():
        total_unread += room.get_unread_count(request.user)
    
    return JsonResponse({'unread_count': total_unread})

@login_required
def message_status_update(request, message_id):
    """Update message status (when receiver sees message)"""
    if request.method == 'POST':
        message = get_object_or_404(Message, id=message_id)
        
        # Only receiver can mark as read
        if message.sender != request.user:
            message.mark_as_read()
            return JsonResponse({'success': True, 'status': 'read'})
    
    return JsonResponse({'success': False})