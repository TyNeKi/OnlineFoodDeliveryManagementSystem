from django import forms
from .models import Admin


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['name', 'email', 'role', 'accessLevel']
        labels = {
            'accessLevel': 'Access Level',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Admin name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'admin@example.com'}),
            'role': forms.TextInput(attrs={'placeholder': 'Admin role'}),
            'accessLevel': forms.TextInput(attrs={'placeholder': 'Full / Read / Write'}),
        }
