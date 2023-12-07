# from django.shortcuts import render

# # Create your views here.

# def index(request):
#     return render(request, "listings/listings.html")


# def listing(request):
#     return render(request, "listings/listing.html")

# def search(request):
#     return render(request, 'listings/search.html')

# #Chapter 23 |  Loop Listing
# from django.shortcuts import render
# from .models import Listing

# # Create your views here.


# def index(request):
#     listings = Listing.objects.all() #take database
#     context = {'listings' : listings} #{}dictionary-look for building
#     return render(request, "listings/listings.html", context) #context-let the context applicable to the page
#     # return render(request, "listings/listings.html")

# #Chapter 24 | Listing by ID
# def listing(request, listing_id): #look for <'int:listing_id>' #request-server request
#     listing = Listing.objects.get(id=listing_id)
#     context = {'listing': listing}
#     return render(request, "listings/listing.html", context)
#     # return render(request, "listings/listing.html")


# # def listing(request):
# #     return render(request, "listings/listing.html")


# def search(request):
#     return render(request, 'listings/search.html')

# # Chapter 26 | Paginator
# from django.shortcuts import render
# from django.core.paginator import Paginator
# from .models import Listing

# # Create your views here.


# def index(request):
#     listings = Listing.objects.all()
#     paginator = Paginator(listings, 3) # Each page 3 records
#     page = request.GET.get('page')
#     page_listings = paginator.get_page(page)
#     # context = {'listings': listings}
#     context = {'listings' : page_listings}
#     return render(request, "listings/listings.html", context)


# def listing(request, listing_id):
#     listing = Listing.objects.get(id=listing_id)
#     context = {'listing': listing}
#     return render(request, "listings/listing.html", context)
#     # return render(request, "listings/listing.html")


# def search(request):
#     return render(request, 'listings/search.html')

# Chapter 27 | 404 for Listing
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# +
from django.http import Http404
# +
from .models import Listing 

# Create your views here.

# ('-list_date')('id')
def index(request):
    listings = Listing.objects.all().order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {'listings' : page_listings}
    return render(request, "listings/listings.html", context)


# def listing(request, listing_id):
#     # listing = Listing.objects.get(id = listing_id)
#     listing = get_object_or_404(Listing, pk=listing_id)
#     context = {'listing' : listing}
#     return render(request, "listings/listing.html", context)

def listing(request, listing_id):
    try: 
        # listing = Listing.objects.get(id = listing_id)
        listing = get_object_or_404(Listing, pk=listing_id)
        context = {'listing' : listing}
        return render(request, "listings/listing.html", context)
    except Http404:
        return render(request, '404.html')


def search(request):
    return render(request, 'listings/search.html')