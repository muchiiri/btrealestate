from django.shortcuts import render
from . models import Listing

def index(request):
    # listings = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    context = {
        'listings': listings
    }
    return render(request, 'listings.html', context)

def listing(request, listing_id):
    return render(request, 'listing.html')

def search(request):
    return render(request, 'search.html')


