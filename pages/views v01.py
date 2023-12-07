### V001 ###
# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.


# def index(request):
#     return HttpResponse("index page")


# def about(request):
#     return HttpResponse("about page")

### V002 ###
# from django.shortcuts import render
# # from django.http import HttpResponse
# # Create your views here.

# def index(request):
#     return render(request, "pages/index.html")
#     #return HttpResponse("index page")

# def about(request):
#     return render(request, "pages/about.html")
#     #return HttpResponse("about page")

# Chapter 28 | Improve drop-down menu in search box
# from django.shortcuts import render
# from django.http import HttpResponse
# from listings.models import Listing
# from listings.choices import price_choices, region_choices, bedroom_choices

# # Create your views here.


# def index(request):
#     listings = Listing.objects.all().order_by('-list_date').filter(is_published=True)[:3]
#     context = {'listings' : listings, 
#                'region_choices' : region_choices, 
#                'price_choices' : price_choices, 
#                'bedroom_choices' : bedroom_choices}
#     return render(request, "pages/index.html", context)
# 		# return HttpResponse("<h1>Hello</h1>")


# def about(request):
#     return render(request, 'pages/about.html')
#     # return HttpResponse("about page")

# Chapter 29 | About
from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, region_choices, bedroom_choices

# Create your views here.


def index(request):
    listings = Listing.objects.all().order_by('-list_date').filter(is_published=True)[:3]
    context = {'listings' : listings, 
               'region_choices' : region_choices, 
               'price_choices' : price_choices, 
               'bedroom_choices' : bedroom_choices}
    return render(request, "pages/index.html", context)
		# return HttpResponse("index page")


def about(request):
		realtors = Realtor.objects.all().order_by('-hire_date')
                
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors' : realtors,
        'mvp_realtors' : mvp_realtors
    }
    return render(request, "pages/about.html", context)
    # return render(request, 'pages/about.html')
    # return HttpResponse("about page")
