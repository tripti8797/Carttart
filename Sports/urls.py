# Import the path function from django.urls to define URL patterns
from django.urls import path
# Import views from the Sports application
from Sports import views


# Define the URL patterns for the application
urlpatterns = [
    path('', views.serviceSports, name='sports'), # Map the 'sports/' URL to the sports view function
]