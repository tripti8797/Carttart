from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm
from .models import User

def user_login(request):
    if request.user.is_authenticated:
        if request.user.is_superadmin:
            return redirect('superadmin_dashboard')
        return redirect('employee_dashboard')

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    auth_login(request, user)
                    messages.success(request, f"Welcome back, {user.full_name}!")
                    
                    if user.is_superadmin:
                        return redirect('superadmin_dashboard')
                    return redirect('employee_dashboard')
                else:
                    messages.error(request, "Invalid credentials")
            except User.DoesNotExist:
                messages.error(request, "User does not exist")
    else:
        form = UserLoginForm()
    
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')