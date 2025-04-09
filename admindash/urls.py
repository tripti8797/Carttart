from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('', dashboard, name='dashboard'),  # Add this line
    path('superadmin/', superadmin_dashboard, name='superadmin_dashboard'),
    path('employee/', employee_dashboard, name='employee_dashboard'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('employees/create/', views.create_employee, name='create_employee'),  # Add Employee URL
    path('employees/', views.manage_employees, name='manage_employees'),  # Manage Employees URL
   path('contact-messages/', views.contact_messages_list, name='contact_messages_list'), 
    path('contact-messages/view/<int:id>/', views.view_message, name='view_message'),
    path('contact-messages/delete/<int:id>/', views.delete_message, name='delete_message'), 
    path('employees/edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),  # Edit Employee
    path('employees/delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),  # Delete Employee
]