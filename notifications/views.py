from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Notification
from .utils import mark_all_as_read

@login_required
def notification_list(request):
    """View all notifications"""
    notifications = Notification.objects.filter(user=request.user)
    
    # Mark as read when viewing all
    if request.GET.get('mark_read') == 'all':
        mark_all_as_read(request.user)
        messages.success(request, 'All notifications marked as read!')
        return redirect('notifications-list')
    
    context = {
        'notifications': notifications,
        'unread_count': notifications.filter(is_read=False).count(),
    }
    return render(request, 'notifications/list.html', context)

@login_required
def notification_detail(request, pk):
    """View single notification and mark as read"""
    notification = get_object_or_404(Notification, pk=pk, user=request.user)
    
    if not notification.is_read:
        notification.mark_as_read()
    
    # Redirect to the link if exists
    if notification.link:
        return redirect(notification.link)
    
    return redirect('notifications-list')

@login_required
def mark_notification_read(request, pk):
    """Mark single notification as read (AJAX)"""
    notification = get_object_or_404(Notification, pk=pk, user=request.user)
    notification.mark_as_read()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success'})
    
    return redirect('notifications-list')

@login_required
def mark_all_read(request):
    """Mark all notifications as read"""
    mark_all_as_read(request.user)
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'count': 0})
    
    messages.success(request, 'All notifications marked as read!')
    return redirect('notifications-list')

@login_required
def delete_notification(request, pk):
    """Delete a notification"""
    notification = get_object_or_404(Notification, pk=pk, user=request.user)
    notification.delete()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success'})
    
    messages.success(request, 'Notification deleted!')
    return redirect('notifications-list')

@login_required
def get_unread_count(request):
    """Get unread notification count (AJAX)"""
    count = Notification.objects.filter(user=request.user, is_read=False).count()
    return JsonResponse({'count': count})