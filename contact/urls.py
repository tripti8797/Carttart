from django.urls import path  # Import the path function to define URL patterns
from . import views  # Import the views module
from django.conf import settings  # Import settings to access media file settings
from django.conf.urls.static import static  # Import function to serve static and media files in development

# Define URL patterns for the application
urlpatterns = [
    path('contact/', views.contactUs.as_view(), name="contact"),  # Maps '/contact/' to the ContactUs class-based view
]
