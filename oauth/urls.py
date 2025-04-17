from django.urls import path
from .views import user_login, logout_view, change_password

urlpatterns = [
    path('login/', user_login, name='login'),
    path('change-password/', change_password, name='change_password'),
    path('logout/', logout_view, name='logout'),
]