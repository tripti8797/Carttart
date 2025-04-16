from django import forms
from .models import ClientLogo

class ClientLogoForm(forms.ModelForm):
    class Meta:
        model = ClientLogo
        fields = [ 'logo', 'sector']