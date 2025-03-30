from django.shortcuts import render, redirect
from .forms import ContactForm  # Import the ContactForm
from .models import ContactMessage  # Import the model if needed
from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib import messages
from django.views import generic

class contactUs(SuccessMessageMixin, generic.CreateView):
    form_class = ContactForm  # The form to be used is the ContactForm
    template_name = "contact.html"  # The template to render the contact form
    success_url = "/"  # Redirect to the home page after a successful form submission
    success_message = "Your query has been submitted successfully, we will contact you soon."  # Success message after submission

    # Override form_invalid to handle invalid form submissions
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please submit the form carefully")  # Error message if the form is invalid
        return redirect('healthcare')