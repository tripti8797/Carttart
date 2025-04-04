from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from oauth.decorators import superadmin_required
from oauth.models import User
from contact.models import ContactMessage
from blog.models import Blog
from .forms import EmployeeCreationForm

def dashboard(request):
    if request.user.is_superadmin:
        return redirect('superadmin_dashboard')
    else:
        return redirect('employee_dashboard')

@login_required
@superadmin_required
def superadmin_dashboard(request):
    messages_list = ContactMessage.objects.all().order_by('-submission_date')[:5]
    employees = User.objects.filter(role='EMPLOYEE')[:5]
    blogs = Blog.objects.all()[:5]
    
    context = {
        'messages': messages_list,
        'employees': employees,
        'blogs': blogs,
        'total_employees': User.objects.filter(role='EMPLOYEE').count(),
        'total_messages': ContactMessage.objects.count(),
        'total_blogs': Blog.objects.count(),
        'username': request.user.username  # Add username to context
    }
    return render(request, 'superadmin_dashboard.html', context)

@login_required
def employee_dashboard(request):
    user_blogs = Blog.objects.filter(author=request.user)
    context = {
        'total_blogs': user_blogs.count(),
    }
    return render(request, 'employee_dashboard.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        try:
            user = request.user
            user.full_name = request.POST.get('full_name', user.full_name)
            user.email = request.POST.get('email', user.email)
            user.phone_number = request.POST.get('phone', user.phone_number)
            user.bio = request.POST.get('bio', user.bio)
            
            if 'profile_picture' in request.FILES:
                user.profile_picture = request.FILES['profile_picture']
            
            user.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('edit_profile')
            
        except Exception as e:
            messages.error(request, f'Error updating profile: {str(e)}')
    
    return render(request, 'edit_profile.html')

@login_required
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.role = 'EMPLOYEE'  # Assign the role as 'EMPLOYEE'
            employee.save()
            return redirect('manage_employees')  # Redirect to the employee list
    else:
        form = EmployeeCreationForm()
    return render(request, 'create_employee.html', {'form': form})

@login_required
@superadmin_required
def manage_employees(request):
    employees = User.objects.filter(role='EMPLOYEE')
    return render(request, 'manage_employees.html', {'employees': employees})

@login_required
@superadmin_required
def contact_messages_list(request):
    messages = ContactMessage.objects.all().order_by('-submission_date')  # Fetch all messages
    return render(request, 'contact_messages_list.html', {'messages': messages})

@login_required
@superadmin_required
def edit_employee(request, employee_id):
    try:
        employee = User.objects.get(id=employee_id, role='EMPLOYEE')
    except User.DoesNotExist:
        messages.error(request, "Employee not found.")
        return redirect('manage_employees')

    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully.")
            return redirect('manage_employees')
    else:
        form = EmployeeCreationForm(instance=employee)

    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})

@login_required
@superadmin_required
def delete_employee(request, employee_id):
    try:
        employee = User.objects.get(id=employee_id, role='EMPLOYEE')
        employee.delete()
        messages.success(request, "Employee deleted successfully.")
    except User.DoesNotExist:
        messages.error(request, "Employee not found.")
    return redirect('manage_employees')