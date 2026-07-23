from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:listing_id>/', views.create_booking, name='create-booking'),
    path('my-bookings/', views.my_bookings, name='my-bookings'),
    path('update/<int:booking_id>/<str:status>/', views.update_booking_status, name='update-booking'),
    path('<int:booking_id>/', views.booking_detail, name='booking-detail'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel-booking'),
]