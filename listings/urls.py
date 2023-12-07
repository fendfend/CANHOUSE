# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='listings'),
#     path('listing', views.listing, name='listing'),
#     path('search', views.search, name="search") ,
# ]

# Chapter 23 | Loop record
from django.urls import path
from . import views
# set the / api, as variable
urlpatterns = [
    path('', views.index, name="listings"),
    # path('listing', views.listing, name='listing'),
    path('<int:listing_id>', views.listing, name='listing'), #<> parameter 
    path('search', views.search, name="search"),
]