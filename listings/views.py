# from django.shortcuts import render

# # Create your views here.

# def index(request):
#     return render(request, "listings/listings.html")


# def listing(request):
#     return render(request, "listings/listing.html")

# def search(request):
#     return render(request, 'listings/search.html')

#Chapter 23 |  Loop Listing
from django.shortcuts import render
from .models import Listing

# Create your views here.


def index(request):
    listings = Listing.objects.all() #take database
    context = {'listings' : listings} #{}dictionary-look for building
    return render(request, "listings/listings.html", context) #context-let the context applicable to the page
    # return render(request, "listings/listings.html")

#Chapter 24 | Listing by ID
def listing(request, listing_id): #look for <'int:listing_id>' #request-server request
    listing = Listing.objects.get(id=listing_id)
    context = {'listing': listing}
    return render(request, "listings/listing.html", context)
    # return render(request, "listings/listing.html")


# def listing(request):
#     return render(request, "listings/listing.html")


def search(request):
    return render(request, 'listings/search.html')