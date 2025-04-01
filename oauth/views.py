from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Hardcoded credentials
CREDENTIALS = {
    "SAD00001": "Carttart@1234",
}
def login_view(request):
    context = {"error": None}
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if credentials match
        if username in CREDENTIALS and CREDENTIALS[username] == password:
            # If credentials match, render the dashboard template
            return render(request, 'dashboard.html', {'username': username})
        else:
            # If credentials don't match, show error
            context["error"] = "Invalid username or password"
    
    # Render the login template
    return render(request, 'login.html', context)


from django.core.paginator import Paginator
from contact.models import ContactMessage

def contact_messages_view(request):
    all_messages = ContactMessage.objects.all().order_by('-submission_date')
    
    # Pagination
    paginator = Paginator(all_messages, 10)  # Show 10 messages per page
    page = request.GET.get('page')
    contact_messages = paginator.get_page(page)
    
    return render(request, 'getintouch.html', {
        'contact_messages': contact_messages,
    })
    
def delete_message(request, message_id):
    if request.method == 'POST':
        message = get_object_or_404(ContactMessage, id=message_id)
        message.delete()
        messages.success(request, "Message deleted successfully")
        # Redirect to the page that shows all messages
        return redirect('contact_messages_view')  # Replace with your actual view name
    # If not POST, redirect to messages page
    return redirect('contact_messages_view')

def dashboard(request):
    # Render the dashboard template
    return render(request, 'dashboard.html')