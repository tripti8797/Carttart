from django.urls import path  # Import the path function to define URL patterns
from Commerce import views  # Import the views module from the Commerce app

# Define URL patterns for the Commerce app
urlpatterns = [
    path('', views.serviceCommerce, name='commerce'),  # Maps '/commerce/' to the commerce view
]
