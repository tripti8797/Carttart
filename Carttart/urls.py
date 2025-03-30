"""
URL configuration for Carttart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Import Django admin
from django.urls import path, include  # Import path and include for URL routing
from django.conf import settings  # Import settings to access static and media file settings
from django.conf.urls.static import static  # Import function to serve static/media files in development

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel route
    path('', include('Home.urls')),  # Home app routing
    path('healthcare', include('Healthcare.urls')),  # Ensure trailing slash for consistency
    path('realestate/', include('Realestate.urls')),  # Real estate app routing
    path('fintech/', include('Fintech.urls')),  # Fintech app routing
    path('energy/', include('Energy.urls')),  # Energy app routing
    path('commerce/', include('Commerce.urls')),  # Commerce app routing
    path('sports/', include('Sports.urls')),  # Sports app routing
    path('tours/', include('Tours.urls')),  # Tours app routing
    path('contact/', include('contact.urls')),  # Contact app routing (Ensure lowercase if app is named `contact`)
    path('blog/', include("blog.urls")),

]


# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # static files handling
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # media files handling
