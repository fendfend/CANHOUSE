### V001 ###
# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.


# def index(request):
#     return HttpResponse("index page")


# def about(request):
#     return HttpResponse("about page")

### V002 ###
from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "pages/index.html")
    #return HttpResponse("index page")

def about(request):
    return render(request, "pages/about.html")
    #return HttpResponse("about page")