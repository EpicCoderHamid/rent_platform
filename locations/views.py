from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import json
from .models import Province, City, UserLocation
from listings.models import Listing
from django.db.models import Q

def location_selector(request):
    """Popup location selector - First page user sees"""
    provinces = Province.objects.all()
    
    context = {
        'provinces': provinces,
    }
    return render(request, 'locations/location_selector.html', context)

@login_required
def save_location(request):
    """Save user selected location"""
    if request.method == 'POST':
        city_id = request.POST.get('city')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        use_live = request.POST.get('use_live_location') == 'on'
        
        user_location, created = UserLocation.objects.get_or_create(
            user=request.user
        )
        
        if city_id:
            city = get_object_or_404(City, id=city_id)
            user_location.city = city
            user_location.province = city.province
            user_location.latitude = city.latitude
            user_location.longitude = city.longitude
            user_location.use_live_location = False
        
        if latitude and longitude:
            user_location.latitude = float(latitude)
            user_location.longitude = float(longitude)
            user_location.use_live_location = True
        
        user_location.save()
        
        # Save to session
        request.session['user_city'] = user_location.city.name if user_location.city else None
        request.session['user_lat'] = user_location.latitude
        request.session['user_lng'] = user_location.longitude
        
        messages.success(request, f'📍 Location set to {user_location.city}')
        return redirect('home')
    
    return redirect('location-select')

@login_required
def update_location(request):
    """Update location from dropdown"""
    if request.method == 'POST':
        city_id = request.POST.get('city')
        
        if city_id:
            city = get_object_or_404(City, id=city_id)
            user_location, created = UserLocation.objects.get_or_create(user=request.user)
            user_location.city = city
            user_location.province = city.province
            user_location.latitude = city.latitude
            user_location.longitude = city.longitude
            user_location.use_live_location = False
            user_location.save()
            
            request.session['user_city'] = city.name
            request.session['user_lat'] = city.latitude
            request.session['user_lng'] = city.longitude
            
            messages.success(request, f'📍 Location updated to {city.name}')
        else:
            messages.error(request, 'Please select a city')
        
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    
    return redirect('home')

@login_required
def set_live_location(request):
    """Set user's live location via GPS"""
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        
        if latitude and longitude:
            user_location, created = UserLocation.objects.get_or_create(
                user=request.user
            )
            user_location.latitude = float(latitude)
            user_location.longitude = float(longitude)
            user_location.use_live_location = True
            user_location.save()
            
            request.session['user_lat'] = float(latitude)
            request.session['user_lng'] = float(longitude)
            
            return JsonResponse({'success': True, 'message': 'Location updated!'})
        
        return JsonResponse({'success': False, 'error': 'Invalid coordinates'})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})

def get_cities_by_province(request):
    """AJAX: Get cities for selected province"""
    province_id = request.GET.get('province_id')
    if province_id:
        cities = City.objects.filter(province_id=province_id).values('id', 'name')
        return JsonResponse(list(cities), safe=False)
    return JsonResponse([], safe=False)

def location_based_search(request):
    """Search items based on user's location"""
    user_city = request.session.get('user_city')
    user_lat = request.session.get('user_lat')
    user_lng = request.session.get('user_lng')
    
    listings = Listing.objects.filter(is_available=True)
    
    if user_city:
        listings = listings.filter(city__icontains=user_city)
    elif user_lat and user_lng:
        listings = listings.filter(
            latitude__isnull=False,
            longitude__isnull=False
        )
    
    search_query = request.GET.get('search')
    if search_query:
        listings = listings.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    category = request.GET.get('category')
    if category:
        listings = listings.filter(category=category)
    
    context = {
        'listings': listings,
        'user_city': user_city,
        'user_lat': user_lat,
        'user_lng': user_lng,
    }
    return render(request, 'locations/location_search.html', context)