from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('abxhs', views.contact_messages_view, name='contact_messages_view'),
    path('delete-message/<int:message_id>/', views.delete_message, name='delete_message'),
]