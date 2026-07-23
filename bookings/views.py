# bookings/views.py - COMPLETELY FIXED
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
from .models import Booking
from listings.models import Listing
from chat.models import ChatRoom, Message
from notifications.utils import send_booking_notification

@login_required
def create_booking(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    
    # Don't allow booking your own item
    if listing.owner == request.user:
        messages.error(request, 'You cannot book your own item!')
        return redirect('listing-detail', pk=listing.id)
    
    if request.method == 'POST':
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
        
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except (ValueError, TypeError):
            messages.error(request, 'Invalid date format!')
            return redirect('listing-detail', pk=listing.id)
        
        if start_date < timezone.now().date():
            messages.error(request, 'Start date cannot be in the past!')
            return redirect('listing-detail', pk=listing.id)
        
        if end_date <= start_date:
            messages.error(request, 'End date must be after start date!')
            return redirect('listing-detail', pk=listing.id)
        
        existing_bookings = Booking.objects.filter(
            listing=listing,
            start_date__lt=end_date,
            end_date__gt=start_date,
            status__in=['pending', 'confirmed']
        )
        
        if existing_bookings.exists():
            messages.error(request, 'These dates are not available!')
            return redirect('listing-detail', pk=listing.id)
        
        days = (end_date - start_date).days
        total_price = days * listing.price_per_day
        
        booking = Booking.objects.create(
            user=request.user,
            listing=listing,
            start_date=start_date,
            end_date=end_date,
            total_price=total_price,
            status='pending'
        )
        
        send_booking_notification(booking, 'created')
        
        # ✅ FIXED #1: Create chat room correctly
        # Check if chat room already exists between these two users for this listing
        existing_rooms = ChatRoom.objects.filter(
            listing=listing,
            participants__id=request.user.id
        ).filter(participants__id=listing.owner.id)
        
        if existing_rooms.exists():
            chat_room = existing_rooms.first()
            created = False
        else:
            chat_room = ChatRoom.objects.create(listing=listing)
            chat_room.participants.add(request.user, listing.owner)
            created = True
        
        if created:
            from notifications.utils import send_notification
            send_notification(
                user=listing.owner,
                title="💬 Chat Room Created",
                message=f"A chat room has been created for you to discuss '{listing.title}' with {request.user.username}",
                notification_type='message',
                link=f'/chat/{chat_room.id}/'
            )
        
        messages.success(request, f'✅ Booking request sent! Total: PKR {total_price} for {days} days')
        messages.info(request, f'💬 You can now chat with the seller to discuss details.')
        return redirect('my-bookings')
    
    return redirect('listing-detail', pk=listing.id)

@login_required
def my_bookings(request):
    bookings_as_buyer = Booking.objects.filter(user=request.user).order_by('-created_at')
    bookings_as_seller = Booking.objects.filter(listing__owner=request.user).order_by('-created_at')
    
    # Add unread message count for each booking (Buyer side)
    for booking in bookings_as_buyer:
        try:
            # ✅ FIXED #2: Use participants__id
            chat_room = ChatRoom.objects.filter(
                listing=booking.listing,
                participants__id=request.user.id
            ).filter(participants__id=booking.listing.owner.id).first()
            
            if chat_room:
                booking.unread_messages = chat_room.messages.filter(
                    is_read=False
                ).exclude(sender=request.user).count()
            else:
                booking.unread_messages = 0
        except:
            booking.unread_messages = 0
    
    # Add unread message count for each booking (Seller side)
    for booking in bookings_as_seller:
        try:
            # ✅ FIXED #3: Use participants__id
            chat_room = ChatRoom.objects.filter(
                listing=booking.listing,
                participants__id=request.user.id
            ).filter(participants__id=booking.user.id).first()
            
            if chat_room:
                booking.unread_messages = chat_room.messages.filter(
                    is_read=False
                ).exclude(sender=request.user).count()
            else:
                booking.unread_messages = 0
        except:
            booking.unread_messages = 0
    
    context = {
        'buyer_bookings': bookings_as_buyer,
        'seller_bookings': bookings_as_seller,
    }
    return render(request, 'bookings/my_bookings.html', context)

@login_required
def update_booking_status(request, booking_id, status):
    booking = get_object_or_404(Booking, id=booking_id)
    
    if booking.listing.owner == request.user:
        booking.status = status
        booking.save()
        
        if status == 'confirmed':
            send_booking_notification(booking, 'confirmed')
            messages.success(request, f'✅ Booking confirmed! {booking.user.username} has been notified.')
            
            # ✅ FIXED #4: Use participants__id
            chat_room = ChatRoom.objects.filter(
                listing=booking.listing,
                participants__id=request.user.id
            ).filter(participants__id=booking.user.id).first()
            
            if chat_room:
                Message.objects.create(
                    chat_room=chat_room,
                    sender=request.user,
                    message=f"📅 Great news! I have confirmed your booking for '{booking.listing.title}' from {booking.start_date} to {booking.end_date}. Feel free to discuss pickup/delivery details here."
                )
                
        elif status == 'cancelled':
            send_booking_notification(booking, 'cancelled')
            messages.warning(request, f'❌ Booking cancelled! {booking.user.username} has been notified.')
            
            # ✅ FIXED #5: Use participants__id
            chat_room = ChatRoom.objects.filter(
                listing=booking.listing,
                participants__id=request.user.id
            ).filter(participants__id=booking.user.id).first()
            
            if chat_room:
                Message.objects.create(
                    chat_room=chat_room,
                    sender=request.user,
                    message=f"⚠️ Sorry, your booking for '{booking.listing.title}' has been cancelled. Please contact me for more information."
                )
                
        elif status == 'completed':
            send_booking_notification(booking, 'completed')
            messages.success(request, f'✅ Booking marked as completed!')
            
            # ✅ FIXED #6: Use participants__id
            chat_room = ChatRoom.objects.filter(
                listing=booking.listing,
                participants__id=request.user.id
            ).filter(participants__id=booking.user.id).first()
            
            if chat_room:
                Message.objects.create(
                    chat_room=chat_room,
                    sender=request.user,
                    message=f"✅ The rental period for '{booking.listing.title}' has been completed. Thank you for choosing our service! Please leave a review."
                )
    
    else:
        messages.error(request, 'You can only update your own listings!')
    
    return redirect('my-bookings')

@login_required
def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    if request.user not in [booking.user, booking.listing.owner]:
        messages.error(request, 'You are not authorized to view this booking!')
        return redirect('my-bookings')
    
    # ✅ FIXED #7: Use participants__id
    chat_room = ChatRoom.objects.filter(
        listing=booking.listing,
        participants__id=booking.user.id
    ).filter(participants__id=booking.listing.owner.id).first()
    
    context = {
        'booking': booking,
        'chat_url': f'/chat/{chat_room.id}/' if chat_room else None,
        'is_owner': request.user == booking.listing.owner,
        'is_buyer': request.user == booking.user,
    }
    return render(request, 'bookings/booking_detail.html', context)

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    if booking.user == request.user and booking.status == 'pending':
        booking.status = 'cancelled'
        booking.save()
        
        from notifications.utils import send_notification
        send_notification(
            user=booking.listing.owner,
            title="❌ Booking Cancelled",
            message=f"{request.user.username} has cancelled their booking for '{booking.listing.title}'",
            notification_type='booking',
            link='/bookings/my-bookings/'
        )
        
        messages.success(request, 'Your booking has been cancelled successfully!')
    else:
        messages.error(request, 'You cannot cancel this booking!')
    
    return redirect('my-bookings')