from django.urls import path  # Import the path function to define URL patterns
from Fintech import views  # Import the views module from the Fintech app

# Define URL patterns for the Fintech app
urlpatterns = [
    path('', views.serviceFintech, name='fintech'),  # Maps '/fintech/' to the fintech view
]
