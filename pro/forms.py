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
    # Client Information Fields
    client_name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'required': 'required'})
    )
    client_company = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name', 'required': 'required'})
    )
    client_email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': 'required'})
    )
    client_phone = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number', 'required': 'required'})
    )
    client_address = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Address'})
    )
    client_industry = forms.ChoiceField(
        choices=[
            ('railway', 'Railway'),
            ('automotive', 'Automotive'),
            ('engineering', 'Engineering'),
            ('other', 'Other')
        ],
        required=True,
        initial='other',
        widget=forms.Select(attrs={'class': 'form-control', 'required': 'required'})
    )

    class Meta:
        model = QuoteRequest
        fields = ['client', 'product', 'width', 'height', 'material', 'finish', 'quantity', 'special_requirements']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control', 'required': False}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'width': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Width in mm', 'step': '0.01'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Height in mm', 'step': '0.01'}),
            'material': forms.Select(attrs={'class': 'form-control'}),
            'finish': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'value': 1}),
            'special_requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Any special requirements...'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make client field optional
        self.fields['client'].required = False
        # Set empty label for client field
        self.fields['client'].empty_label = "-- Select an existing client or leave empty for new customer --"