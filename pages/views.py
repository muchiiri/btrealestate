from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) [:3]

    context = {
        'listings': listings
    }

    return render(request, 'index.html', context)


def about(request):
    realtors = Realtor.objects.all()

    context = {
        'realtors' : realtors
    }

    return render(request, 'about.html', context)
