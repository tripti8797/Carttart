from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from .forms import UserLoginForm, CustomPasswordChangeForm
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
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # keeps user logged in after change
            messages.success(request, "Password changed successfully!")
            return redirect('superadmin_dashboard')  # or anywhere you want
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})



@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')