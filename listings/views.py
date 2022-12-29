from django.shortcuts import render
from . models import Listing

def index(request):
    listings = Listing.objects.all()

    context = {
        'listings': listings
    }
    return render(request, 'listings.html', context)

def listing(request):
    return render(request, 'listing.html')

def search(request):
    return render(request, 'search.html')


