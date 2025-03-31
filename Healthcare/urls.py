from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

# Import views from the Healthcare application
from Healthcare import views

# Define the URL patterns for the application
urlpatterns = [
    path('', views.serviceHealthcare, name='healthcare'),  # Map the 'healthcare/' URL to the healthcare view function
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)