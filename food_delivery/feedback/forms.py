from django import forms

from .models import Complaint


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['customerID', 'orderID', 'adminID', 'description', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
