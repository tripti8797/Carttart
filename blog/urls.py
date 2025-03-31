from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # commerce blog list and detail
    path("commerce/", views.blog_list, {"blog_type": "commerce"}, name="commerce_blog_list"),
    re_path(r"^commerce/(?P<slug>[-\w]+)/$", views.blog_detail, {"blog_type": "commerce"}, name="commerce_blog_detail"),

    # energy blog list and detail
    path("energy/", views.blog_list, {"blog_type": "energy"}, name="energy_blog_list"),
    re_path(r"^energy/(?P<slug>[-\w]+)/$", views.blog_detail, {"blog_type": "energy"}, name="energy_blog_detail"),

    # esports blog list and detail
    path("esports/", views.blog_list, {"blog_type": "esports"}, name="esports_blog_list"),
    re_path(r"^esports/(?P<slug>[-\w]+)/$", views.blog_detail, {"blog_type": "esports"}, name="esports_blog_detail"),

    # fintech blog list and detail
    path("fintech/", views.blog_list, {"blog_type": "fintech"}, name="fintech_blog_list"),
    re_path(r"^fintech/(?P<slug>[-\w]+)/$", views.blog_detail, {"blog_type": "fintech"}, name="fintech_blog_detail"),

    # healthcare blog list and detail
    path("healthcare/", views.blog_list, {"blog_type": "healthcare"}, name="healthcare_blog_list"),
    re_path(r"^healthcare/(?P<slug>[-\w]+)/$", views.blog_detail, {"blog_type": "healthcare"}, name="healthcare_blog_detail"),

    # realestate blog list and detail
    path("realestate/", views.blog_list, {"blog_type": "realestate"}, name="realestate_blog_list"),
    re_path(r"^realestate/(?P<slug>[-\w]+)/$", views.blog_detail, {"blog_type": "realestate"}, name="realestate_blog_detail"),

    # tour blog list and detail
    path("tour/", views.blog_list, {"blog_type": "tour"}, name="tour_blog_list"),
    re_path(r"^tour/(?P<slug>[-\w]+)/$", views.blog_detail, {"blog_type": "tour"}, name="tour_blog_detail"),
    
    # Blog creation and management
    path("form/", views.form, name="form"),
    path("manage-blogs/", views.manage_blogs, name="manage_blogs"),
    path("toggle_blog_status/<int:blog_id>/", views.toggle_blog_status, name="toggle_blog_status"),
    path("edit_blog/<int:blog_id>/", views.edit_blog, name="edit_blog"),
    path("delete_blog/<int:blog_id>/", views.delete_blog, name="delete_blog"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)