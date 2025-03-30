# Import the render function from django.shortcuts to render templates
from django.shortcuts import render
from blog.models import Blog
from django.utils.text import slugify

# This function handles requests to the 'healthcare/' URL and renders the healthcare.html template.
# Define the healthcare view function
def serviceHealthcare(request):
    # Get healthcare blogs
    blogs = Blog.objects.filter(active=True, blog_type='healthcare').order_by("-published_date")
    
    # Validate and fix slugs if needed
    for blog in blogs:
        if not blog.slug or not slugify(blog.slug):
            blog.slug = slugify(blog.title)
            blog.save()
    
    return render(request, "healthcare.html", {"blogs": blogs})