# listings/views.py - Complete Smart Search System
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Avg
from django.core.paginator import Paginator
from .models import Listing, Review
from .forms import ListingForm, ReviewForm
from notifications.utils import send_notification, send_review_notification
from .spell_checker import SpellChecker
import re

def home(request):
    """Home page - shows all available listings"""
    listings_list = Listing.objects.filter(is_available=True).order_by('-created_at')
    
    if request.user.is_authenticated:
        try:
            if not request.user.location or not request.user.location.city:
                return redirect('location-select')
        except:
            return redirect('location-select')
    
    user_city = request.session.get('user_city')
    user_lat = request.session.get('user_lat')
    user_lng = request.session.get('user_lng')
    
    if user_city:
        listings_list = listings_list.filter(city__icontains=user_city)
    elif user_lat and user_lng:
        listings_list = listings_list.filter(latitude__isnull=False, longitude__isnull=False)
    
    search_query = request.GET.get('search')
    if search_query:
        listings_list = listings_list.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(city__icontains=search_query)
        )
    
    paginator = Paginator(listings_list, 100)
    page_number = request.GET.get('page')
    listings = paginator.get_page(page_number)
    
    context = {
        'listings': listings,
        'categories': Listing.CATEGORY_CHOICES,
        'search_query': search_query,
        'user_city': user_city,
        'show_location_banner': True,
    }
    return render(request, 'listings/home.html', context)

def smart_search(request):
    """AI-Powered Smart Search with Spell Check & Location Fallback"""
    
    query = request.GET.get('q', '').strip()
    original_query = query
    
    search_context = {
        'original_query': original_query,
        'corrected_query': None,
        'was_corrected': False,
        'suggestions': [],
        'detected_city': None,
        'detected_category': None,
        'detected_price_min': None,
        'detected_price_max': None,
        'detected_sort': None,
        'used_fallback': False,
        'fallback_message': None,
        'available_cities': [],
    }
    
    temp_results = {'location_based': None, 'all_pakistan': None, 'similar_items': None}
    
    if query:
        # Step 1: Spell Correction
        corrected_query, was_corrected = SpellChecker.correct_query(query)
        if was_corrected:
            search_context['corrected_query'] = corrected_query
            search_context['was_corrected'] = True
            search_context['suggestions'] = SpellChecker.get_suggestions(query)
            query_to_search = corrected_query
        else:
            query_to_search = query
        
        query_lower = query_to_search.lower()
        
        # Step 2: Detect City
        cities = ['karachi', 'lahore', 'islamabad', 'rawalpindi', 'multan', 
                  'faisalabad', 'gujranwala', 'peshawar', 'quetta', 'sialkot']
        
        for city in cities:
            if city in query_lower:
                search_context['detected_city'] = city.title()
                query_lower = query_lower.replace(city, '').strip()
                break
        
        # Step 3: Detect Category
        categories = {
            'electronics': ['electronics', 'mobile', 'phone', 'iphone', 'samsung', 'laptop', 'computer'],
            'furniture': ['furniture', 'sofa', 'bed', 'table', 'chair', 'desk'],
            'vehicles': ['vehicles', 'car', 'bike', 'motorcycle', 'gari', 'toyota', 'honda'],
            'clothing': ['clothing', 'dress', 'shirt', 'pant', 'kurta', 'lawn'],
            'books': ['books', 'novel', 'textbook', 'quran'],
        }
        
        for cat_key, keywords in categories.items():
            for keyword in keywords:
                if keyword in query_lower:
                    search_context['detected_category'] = cat_key.title()
                    query_lower = query_lower.replace(keyword, '').strip()
                    break
            if search_context['detected_category']:
                break
        
        # Step 4: Detect Price
        under_match = re.search(r'under\s+(\d+)', query_lower)
        if under_match:
            search_context['detected_price_max'] = int(under_match.group(1))
            query_lower = re.sub(r'under\s+\d+', '', query_lower).strip()
        
        range_match = re.search(r'(\d+)\s*(?:to|-)\s*(\d+)', query_lower)
        if range_match:
            search_context['detected_price_min'] = int(range_match.group(1))
            search_context['detected_price_max'] = int(range_match.group(2))
            query_lower = re.sub(r'\d+\s*(?:to|-)\s*\d+', '', query_lower).strip()
        
        # Step 5: Detect Sort
        if 'newest' in query_lower or 'latest' in query_lower:
            search_context['detected_sort'] = 'newest'
        elif 'cheap' in query_lower or 'sasta' in query_lower:
            search_context['detected_sort'] = 'price_low'
        elif 'expensive' in query_lower or 'mehnga' in query_lower:
            search_context['detected_sort'] = 'price_high'
        
        # Step 6: Build Filter Function
        def apply_filters(listings, city=None, category=None, price_min=None, price_max=None):
            if city:
                listings = listings.filter(city__icontains=city)
            if category:
                listings = listings.filter(category=category.lower())
            if price_min:
                listings = listings.filter(price_per_day__gte=price_min)
            if price_max:
                listings = listings.filter(price_per_day__lte=price_max)
            
            if query_lower and len(query_lower) > 2:
                words = query_lower.split()
                for word in words:
                    if len(word) > 2:
                        listings = listings.filter(
                            Q(title__icontains=word) |
                            Q(description__icontains=word)
                        )
            return listings
        
        base_listings = Listing.objects.filter(is_available=True)
        
        # Step 7: Search Logic with Fallback
        if search_context['detected_city']:
            location_results = apply_filters(
                base_listings,
                city=search_context['detected_city'].lower(),
                category=search_context['detected_category'].lower() if search_context['detected_category'] else None,
                price_min=search_context['detected_price_min'],
                price_max=search_context['detected_price_max']
            )
            temp_results['location_based'] = location_results
            
            if location_results.exists():
                final_listings = location_results
                search_context['used_fallback'] = False
            else:
                all_results = apply_filters(
                    base_listings,
                    category=search_context['detected_category'].lower() if search_context['detected_category'] else None,
                    price_min=search_context['detected_price_min'],
                    price_max=search_context['detected_price_max']
                )
                temp_results['all_pakistan'] = all_results
                
                if all_results.exists():
                    available_cities = list(all_results.values_list('city', flat=True).distinct()[:5])
                    search_context['available_cities'] = available_cities
                    search_context['fallback_message'] = f"No {search_context['detected_category'] or 'items'} found in {search_context['detected_city']}. Showing results from all Pakistan."
                    search_context['used_fallback'] = True
                    final_listings = all_results
                else:
                    final_listings = base_listings.none()
        else:
            final_listings = apply_filters(
                base_listings,
                category=search_context['detected_category'].lower() if search_context['detected_category'] else None,
                price_min=search_context['detected_price_min'],
                price_max=search_context['detected_price_max']
            )
        
        # Step 8: Apply Sorting
        if search_context['detected_sort'] == 'newest':
            final_listings = final_listings.order_by('-created_at')
        elif search_context['detected_sort'] == 'price_low':
            final_listings = final_listings.order_by('price_per_day')
        elif search_context['detected_sort'] == 'price_high':
            final_listings = final_listings.order_by('-price_per_day')
        else:
            final_listings = final_listings.order_by('-created_at')
        
        # Step 9: No results - show similar
        if not final_listings.exists() and search_context['detected_category']:
            similar_items = Listing.objects.filter(
                category=search_context['detected_category'].lower(),
                is_available=True
            )[:6]
            temp_results['similar_items'] = similar_items
            search_context['fallback_message'] = f"No exact matches. Showing similar {search_context['detected_category']} items."
            search_context['used_fallback'] = True
            final_listings = similar_items
    
    else:
        final_listings = Listing.objects.filter(is_available=True).order_by('-created_at')
    
    # Pagination
    paginator = Paginator(final_listings, 12)
    page_number = request.GET.get('page')
    listings = paginator.get_page(page_number)
    
    context = {
        'listings': listings,
        'search_query': original_query,
        'search_context': search_context,
        'temp_results': temp_results,
        'result_count': final_listings.count() if hasattr(final_listings, 'count') else 0,
    }
    return render(request, 'listings/smart_search_results.html', context)

# ========== OTHER VIEWS (keep your existing views) ==========

def listing_list(request):
    listings = Listing.objects.select_related('owner').filter(is_available=True)
    
    user_city = request.session.get('user_city')
    search_query = request.GET.get('search')
    if search_query:
        listings = listings.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(city__icontains=search_query)
        )
    
    city = request.GET.get('city')
    if city:
        listings = listings.filter(city__icontains=city)
    elif user_city and not city:
        listings = listings.filter(city__icontains=user_city)
    
    category = request.GET.get('category')
    if category:
        listings = listings.filter(category=category)
    
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        listings = listings.filter(price_per_day__gte=min_price)
    if max_price:
        listings = listings.filter(price_per_day__lte=max_price)
    
    sort_by = request.GET.get('sort')
    if sort_by == 'price_low':
        listings = listings.order_by('price_per_day')
    elif sort_by == 'price_high':
        listings = listings.order_by('-price_per_day')
    elif sort_by == 'newest':
        listings = listings.order_by('-created_at')
    
    paginator = Paginator(listings, 12)
    page_number = request.GET.get('page')
    listings = paginator.get_page(page_number)
    
    context = {
        'listings': listings,
        'search_query': search_query,
        'city': city or user_city,
        'category': category,
        'min_price': min_price,
        'max_price': max_price,
        'sort_by': sort_by,
        'user_city': user_city,
    }
    return render(request, 'listings/listing_list.html', context)

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    reviews = listing.reviews.all()
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    
    similar_items = Listing.objects.filter(
        category=listing.category,
        is_available=True
    ).exclude(id=listing.id)[:3]
    
    chat_url = None
    if request.user.is_authenticated and request.user != listing.owner:
        try:
            from chat.models import ChatRoom
            chat_room = ChatRoom.objects.filter(
                listing=listing,
                participants=request.user
            ).filter(participants=listing.owner).first()
            if chat_room:
                chat_url = f'/chat/{chat_room.id}/'
        except:
            chat_url = None
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.listing = listing
            review.user = request.user
            review.save()
            if request.user != listing.owner:
                send_review_notification(review)
            messages.success(request, 'Your review has been added!')
            return redirect('listing-detail', pk=pk)
    else:
        form = ReviewForm()
    
    context = {
        'listing': listing,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'form': form,
        'chat_url': chat_url,
        'similar_items': similar_items,
    }
    return render(request, 'listings/listing_detail.html', context)

@login_required
def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            if hasattr(request.user, 'location') and request.user.location.city:
                if not listing.city:
                    listing.city = request.user.location.city.name
            listing.save()
            messages.success(request, 'Your item has been listed successfully!')
            return redirect('listing-detail', pk=listing.pk)
    else:
        form = ListingForm()
    return render(request, 'listings/listing_form.html', {'form': form, 'title': 'Add New Item'})

@login_required
def listing_edit(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if listing.owner != request.user:
        messages.error(request, 'You can only edit your own listings!')
        return redirect('listing-list')
    
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your item has been updated!')
            return redirect('listing-detail', pk=pk)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/listing_form.html', {'form': form, 'title': 'Edit Item'})

@login_required
def listing_delete(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if listing.owner == request.user:
        listing.delete()
        messages.success(request, 'Your item has been deleted!')
    else:
        messages.error(request, 'You can only delete your own listings!')
    return redirect('listing-list')

@login_required
def my_listings(request):
    listings = Listing.objects.filter(owner=request.user).order_by('-created_at')
    paginator = Paginator(listings, 10)
    page_number = request.GET.get('page')
    listings = paginator.get_page(page_number)
    context = {'listings': listings}
    return render(request, 'listings/my_listings.html', context)

@login_required
def toggle_availability(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if listing.owner != request.user:
        messages.error(request, 'You can only modify your own listings!')
        return redirect('listing-list')
    listing.is_available = not listing.is_available
    listing.save()
    status = "available" if listing.is_available else "unavailable"
    messages.success(request, f'Your item is now {status}!')
    return redirect('my-listings')

@login_required
def nearby_items(request):
    user_lat = request.session.get('user_lat')
    user_lng = request.session.get('user_lng')
    if not user_lat or not user_lng:
        messages.error(request, 'Please enable location services first!')
        return redirect('location-select')
    listings = Listing.objects.filter(is_available=True, latitude__isnull=False, longitude__isnull=False)
    radius = request.GET.get('radius', 50)
    context = {'listings': listings, 'user_lat': user_lat, 'user_lng': user_lng, 'radius': radius}
    return render(request, 'listings/nearby_items.html', context)