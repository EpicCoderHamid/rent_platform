from django.urls import path
from . import views

urlpatterns = [
    path('', views.notification_list, name='notifications-list'),
    path('<int:pk>/', views.notification_detail, name='notification-detail'),
    path('<int:pk>/read/', views.mark_notification_read, name='notification-read'),
    path('mark-all-read/', views.mark_all_read, name='notifications-mark-all'),
    path('<int:pk>/delete/', views.delete_notification, name='notification-delete'),
    path('unread-count/', views.get_unread_count, name='unread-count'),
]