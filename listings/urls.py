# listings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listings/', views.listing_list, name='listing-list'),
    path('listing/<int:pk>/', views.listing_detail, name='listing-detail'),
    path('listing/new/', views.listing_create, name='listing-create'),
    path('listing/<int:pk>/edit/', views.listing_edit, name='listing-edit'),
    path('listing/<int:pk>/delete/', views.listing_delete, name='listing-delete'),
    path('my-listings/', views.my_listings, name='my-listings'),
    path('toggle-availability/<int:pk>/', views.toggle_availability, name='toggle-availability'),
    path('nearby/', views.nearby_items, name='nearby-items'),
    path('search/', views.smart_search, name='smart-search'),  # ✅ Add this
]