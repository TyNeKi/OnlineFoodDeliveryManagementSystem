from django import forms

from .models import Complaint


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['customerID', 'orderID', 'adminID', 'description', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class ReviewForm(forms.Form):
    delivery_id = forms.CharField(
        label='Delivery ID',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter delivery ID or order reference'})
    )
    rating = forms.IntegerField(
        label='Rating',
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'placeholder': '1-5'})
    )
    comment = forms.CharField(
        label='Comment',
        required=False,
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe your delivery experience'})
    )
