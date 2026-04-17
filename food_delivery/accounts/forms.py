from django import forms
from .models import Admin


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['name', 'email', 'role', 'accessLevel']
        widgets = {
            'accessLevel': forms.Select(),
        }
