from django.urls import path
from clientlogo import views

urlpatterns = [
    path('upload/', views.upload_logo, name='upload_logo'),
    path('home/', views.logo_slider, name='logo_slider'), 
    path('edit/<int:pk>/', views.edit_logo, name='edit_logo'),
    path('delete/<int:pk>/', views.delete_logo, name='delete_logo'),
]