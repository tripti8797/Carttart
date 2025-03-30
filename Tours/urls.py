# Import the path function from django.urls to define URL patterns
from django.urls import path

# Import views from the Tours application
from Tours import views

# Define the URL patterns for the application
urlpatterns = [
    path('', views.serviceTours, name='tours'),  # Map the 'tours/' URL to the tours view function
]