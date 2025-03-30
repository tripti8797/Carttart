# Import the render function from django.shortcuts to render templates
from django.shortcuts import render
from blog.models import Blog
from django.utils.text import slugify

# Define the realstate view function realestate
def serviceRealestate(request):
    # Get realestate blogs
    blogs = Blog.objects.filter(active=True, blog_type='realestate').order_by("-published_date")
    
    # Validate and fix slugs if needed
    for blog in blogs:
        if not blog.slug or not slugify(blog.slug):
            blog.slug = slugify(blog.title)
            blog.save()
    
    return render(request, "realestate.html", {"blogs": blogs})