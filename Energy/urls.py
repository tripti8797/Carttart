from django.urls import path  # Import the path function to define URL patterns
from Energy import views  # Import the views module from the Energy app

# Define URL patterns for the Energy app
urlpatterns = [
    path('', views.serviceEnergy, name='energy'),  # Maps '/energy/' to the energy view
]
