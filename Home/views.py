from django.shortcuts import render  # Import the render function to render HTML templates
from django.http import HttpResponse  # Import HttpResponse (not used in this file but generally useful for returning responses)
from clientlogo.models import ClientLogo  # Import the ClientLogo model to fetch client logos

# View function for the home page
def index(request):
    logos = ClientLogo.objects.all()  # ✅ Properly fetches all ClientLogo objects
    return render(request, 'index.html', {"logos": logos})

# View function for the About page
def about(request):
    return render(request, 'about.html')  # Renders the "maintenance.html" template (placeholder)

# View function for the Terms and Conditions page
def termsCond(request):
    return render(request, 't&c.html')  # Renders the "maintenance.html" template (placeholder)

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
    return render(request, 'policy.html')  # Renders the "maintenance.html" template (placeholder)

def maintainence(request):
    return render(request, 'maintenance.html')  # Renders the "maintenance.html" template (placeholder)