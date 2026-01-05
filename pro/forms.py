from django import forms
from .models import Client, QuoteRequest

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'company', 'email', 'phone', 'address', 'industry']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Address'}),
            'industry': forms.Select(attrs={'class': 'form-control'}),
        }

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['client', 'product', 'width', 'height', 'material', 'finish', 'quantity', 'special_requirements']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'width': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Width in mm'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Height in mm'}),
            'material': forms.Select(attrs={'class': 'form-control'}),
            'finish': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'value': 1}),
            'special_requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Any special requirements...'}),
        }