from django.urls import path
from . import views

urlpatterns = [
    path('select/', views.location_selector, name='location-select'),
    path('save/', views.save_location, name='save-location'),
    path('update/', views.update_location, name='update-location'),
    path('set-live/', views.set_live_location, name='set-live-location'),
    path('get-cities/', views.get_cities_by_province, name='get-cities'),
    path('search/', views.location_based_search, name='location-search'),
]