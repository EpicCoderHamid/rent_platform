from .models import Notification

def send_notification(user, title, message, notification_type='system', link=None):
    """Send notification to a specific user"""
    try:
        notification = Notification.objects.create(
            user=user,
            title=title,
            message=message,
            notification_type=notification_type,
            link=link
        )
        return notification
    except Exception as e:
        print(f"Error sending notification: {e}")
        return None

def send_booking_notification(booking, action):
    """Send booking related notifications"""
    
    if action == 'created':
        # To Seller (Item owner)
        send_notification(
            user=booking.listing.owner,
            title="📅 New Booking Request!",
            message=f"{booking.user.username} wants to rent your '{booking.listing.title}' from {booking.start_date} to {booking.end_date}",
            notification_type='booking',
            link='/bookings/my-bookings/'
        )
        
        # To Buyer (Who booked)
        send_notification(
            user=booking.user,
            title="✅ Booking Request Sent",
            message=f"Your request to rent '{booking.listing.title}' has been sent to the seller. Waiting for confirmation.",
            notification_type='booking',
            link='/bookings/my-bookings/'
        )
    
    elif action == 'confirmed':
        # To Buyer
        send_notification(
            user=booking.user,
            title="🎉 Booking Confirmed!",
            message=f"Great news! Your booking for '{booking.listing.title}' has been confirmed. Get ready to enjoy!",
            notification_type='booking',
            link=f'/listings/{booking.listing.id}/'
        )
    
    elif action == 'cancelled':
        # To Buyer
        send_notification(
            user=booking.user,
            title="❌ Booking Cancelled",
            message=f"Sorry, your booking for '{booking.listing.title}' has been cancelled by the seller.",
            notification_type='booking',
            link='/bookings/my-bookings/'
        )
    
    elif action == 'completed':
        # To Both
        send_notification(
            user=booking.user,
            title="📝 Booking Completed",
            message=f"Your rental period for '{booking.listing.title}' has ended. Please return the item and leave a review!",
            notification_type='booking',
            link=f'/listings/{booking.listing.id}/'
        )
        send_notification(
            user=booking.listing.owner,
            title="📝 Booking Completed",
            message=f"{booking.user.username}'s booking for '{booking.listing.title}' has been completed.",
            notification_type='booking',
            link='/bookings/my-bookings/'
        )

def send_review_notification(review):
    """Send notification when a review is posted"""
    send_notification(
        user=review.listing.owner,
        title="⭐ New Review Received",
        message=f"{review.user.username} rated your '{review.listing.title}' {review.rating} stars: '{review.comment[:100]}'",
        notification_type='review',
        link=f'/listings/{review.listing.id}/'
    )

def send_message_notification(user, from_user, listing_title):
    """Send notification for new message (for chat feature)"""
    send_notification(
        user=user,
        title="💬 New Message",
        message=f"{from_user.username} sent you a message about '{listing_title}'",
        notification_type='message',
        link='/messages/'
    )

def mark_all_as_read(user):
    """Mark all notifications as read for a user"""
    Notification.objects.filter(user=user, is_read=False).update(is_read=True)