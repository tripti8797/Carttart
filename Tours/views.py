# Import the render function from django.shortcuts to render templates
from django.shortcuts import render
from blog.models import Blog
from django.utils.text import slugify
from clientlogo.models import ClientLogo

# Define the tours view function tours
def serviceTours(request):
    blogs = Blog.objects.filter(active=True, blog_type='tour').order_by("-published_date")
    print("Blogs fetched:", blogs)
         # Get healthcare logos
    logos = ClientLogo.objects.filter(sector='tourism')
    
    # Validate and fix slugs if needed
    for blog in blogs:
        if not blog.slug or not slugify(blog.slug):
            blog.slug = slugify(blog.title)
            blog.save()
    
  # Render template with blogs and logos
    return render(request, "tours.html", {"blogs": blogs, "logos": logos})