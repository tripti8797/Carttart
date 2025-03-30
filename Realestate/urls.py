# Import the path function from django.urls to define URL patterns
from django.urls import path

# Import views from the Realestate application
from Realestate import views


# Define the URL patterns for the application
urlpatterns = [
    path('', views.serviceRealestate, name='realestate'), # Map the 'realestate/' URL to the realestate view function
]