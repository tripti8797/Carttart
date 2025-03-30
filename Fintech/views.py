from django.shortcuts import render  # Import the render function to render HTML templates
from blog.models import Blog
from django.utils.text import slugify

# View function for the Fintech page
def serviceFintech(request):
    # Get fintech blogs
    blogs = Blog.objects.filter(active=True, blog_type='fintech').order_by("-published_date")
    
    # Validate and fix slugs if needed
    for blog in blogs:
        if not blog.slug or not slugify(blog.slug):
            blog.slug = slugify(blog.title)
            blog.save()
    
    return render(request, "fintech.html", {"blogs": blogs})