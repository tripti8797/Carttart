from django.shortcuts import render  # Import the render function to render HTML templates
from django.http import HttpResponse  # Import HttpResponse (not used in this file but generally useful for returning responses)

# View function for the home page
def index(request):
    return render(request, 'index.html')  # Renders the "index.html" template

# View function for the About page
def about(request):
    return render(request, 'maintenance.html')  # Renders the "maintenance.html" template (placeholder)

# View function for the Terms and Conditions page
def termsCond(request):
    return render(request, 'maintenance.html')  # Renders the "maintenance.html" template (placeholder)

# View function for the Testimonials page
def testimonials(request):
    return render(request, 'maintenance.html')  # Renders the "maintenance.html" template (placeholder)

# View function for the Career page
def career(request):
    return render(request, 'maintenance.html')  # Renders the "maintenance.html" template (placeholder)

# View function for the Child Policy page
def child_policy(request):
    return render(request, 'maintenance.html')  # Renders the "maintenance.html" template (placeholder)

# View function for the Privacy Policy page
def privacy_policy(request):
    return render(request, 'maintenance.html')  # Renders the "maintenance.html" template (placeholder)
