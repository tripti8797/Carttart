# healthcare/views.py
from django.shortcuts import render
from blog.models import Blog
from django.utils.text import slugify

def serviceHealthcare(request):
    # Get healthcare blogs
    blogs = Blog.objects.filter(active=True, blog_type='healthcare').order_by("-published_date")
    print("Blogs fetched:", blogs)  # This will help you check if the queryset is empty or has data
    if not blogs:
        return render(request, "healthcare.html", {"message": "No healthcare blogs found."})

    # Validate and fix slugs if needed
    for blog in blogs:
        if not blog.slug or not slugify(blog.slug):
            blog.slug = slugify(blog.title)
            blog.save()
    return render(request, "healthcare.html", {"blogs": blogs})