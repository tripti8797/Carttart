from django.shortcuts import render, redirect, get_object_or_404
from .models import ClientLogo
from django.http import HttpResponse
from .forms import ClientLogoForm

def logo_slider(request):
    logos = ClientLogo.objects.all()
    return render(request, 'slider.html', {'logos': logos})

def upload_logo(request):
    if request.method == 'POST':
        form = ClientLogoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success = True
            return redirect('upload_logo')  # redirect to slider view
    else:
        form = ClientLogoForm()
    return render(request, 'upload.html', {'form': form})

def edit_logo(request, pk):
    logo = get_object_or_404(ClientLogo, pk=pk)
    if request.method == 'POST':
        form = ClientLogoForm(request.POST, request.FILES, instance=logo)
        if form.is_valid():
            form.save()
            return redirect('logo_slider')
    else:
        form = ClientLogoForm(instance=logo)
    return render(request, 'edit_logo.html', {'form': form})

def delete_logo(request, pk):
    logo = get_object_or_404(ClientLogo, pk=pk)
    if request.method == 'POST':
        logo.delete()
        return redirect('logo_slider')
    return render(request, 'confirm_delete.html', {'logo': logo})