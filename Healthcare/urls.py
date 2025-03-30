# Import the path function from django.urls to define URL patterns
from django.urls import path

# Import views from the Healthcare application
from Healthcare import views

# Define the URL patterns for the application
urlpatterns = [
    path('', views.serviceHealthcare, name='healthcare'), # Map the 'healthcare/' URL to the healthcare view function
]