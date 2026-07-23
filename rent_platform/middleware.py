from django.shortcuts import redirect
from django.urls import reverse

class LocationCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip for admin and location pages
        if request.user.is_authenticated:
            if not request.path.startswith('/locations/') and not request.path.startswith('/admin/'):
                if not hasattr(request.user, 'location') or not request.user.location.city:
                    return redirect('location-select')
        
        return self.get_response(request)