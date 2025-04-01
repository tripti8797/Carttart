from django.urls import path  # Import the path function to define URL patterns
from Home import views  # Import the views module from the Home app

# Define URL patterns for the application
urlpatterns = [
    path('', views.index, name='home'),  # Maps the root URL to the home view
    path('about/', views.about, name='about'),  # Maps '/about/' to the about view
    path('t&c/', views.termsCond, name='t&c'),  # Maps '/t&c/' to the terms and conditions view
    path('testimonials/', views.testimonials, name='testimonials'),  # Maps '/testimonials/' to the testimonials view
    path('career/', views.career, name='career'),  # Maps '/career/' to the career view
    path('child_policy/', views.child_policy, name='child_policy'),  # Maps '/child_policy/' to the child policy view
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),  # Maps '/privacy_policy/' to the privacy policy view
    path('maintainence/', views.maintainence, name='maintainence'),  # Maps '/maintainence/' to the maintenance view
]
