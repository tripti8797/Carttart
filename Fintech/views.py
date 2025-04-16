from django.shortcuts import render  # Import the render function to render HTML templates
from blog.models import Blog
from django.utils.text import slugify
from clientlogo.models import ClientLogo

# View function for the Fintech page
def serviceFintech(request):
    # Get fintech blogs
    blogs = Blog.objects.filter(active=True, blog_type='fintech').order_by("-published_date")
    print("Blogs fetched:", blogs)
      # Get healthcare logos
    logos = ClientLogo.objects.filter(sector='fintech')
    # Validate and fix slugs if needed
    for blog in blogs:
        if not blog.slug or not slugify(blog.slug):
            blog.slug = slugify(blog.title)
            blog.save()


    # Render template with blogs and logos
    return render(request, "fintech.html", {"blogs": blogs, "logos": logos})