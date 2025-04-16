from django.shortcuts import render
from blog.models import Blog
from django.utils.text import slugify
from clientlogo.models import ClientLogo

def serviceHealthcare(request):
    # Get healthcare blogs
    blogs = Blog.objects.filter(active=True, blog_type='healthcare').order_by("-published_date")
    print("Blogs fetched:", blogs)

    # Get healthcare logos
    logos = ClientLogo.objects.filter(sector='healthcare')

    # Validate and fix slugs if needed
    for blog in blogs:
        if not blog.slug or not slugify(blog.slug):
            blog.slug = slugify(blog.title)
            blog.save()

    # Render template with blogs and logos
    return render(request, "healthcare.html", {"blogs": blogs, "logos": logos})