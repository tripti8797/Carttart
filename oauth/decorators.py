from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def superadmin_required(view_func):
    """
    Decorator that checks if the user is a superadmin.
    Redirects to login page if not authenticated, or to employee dashboard if not superadmin.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "You need to login first")
            return redirect('login')
        
        if not request.user.is_superadmin:
            messages.error(request, "You don't have permission to access this page")
            return redirect('employee_dashboard')
        
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def employee_required(view_func):
    """
    Decorator that checks if the user is an employee.
    Redirects to login page if not authenticated, or to superadmin dashboard if superadmin.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "You need to login first")
            return redirect('login')
        
        if request.user.is_superadmin:
            messages.error(request, "Superadmins should use their dashboard")
            return redirect('superadmin_dashboard')
        
        return view_func(request, *args, **kwargs)
    return _wrapped_view