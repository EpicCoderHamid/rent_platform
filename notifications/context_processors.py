from .models import Notification

def notification_context(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user)[:8]
        unread_count = Notification.objects.filter(user=request.user, is_read=False).count()
        return {
            'notifications': notifications,
            'unread_count': unread_count
        }
    return {'notifications': [], 'unread_count': 0}