from django import forms
from django.contrib.auth.models import User
from .models import Admin


class AdminForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        label='Password',
        required=True,
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
        label='Confirm Password',
        required=True,
    )

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

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')

        email = cleaned_data.get('email')
        if email and User.objects.filter(username=email).exists():
            raise forms.ValidationError('A user with this email already exists.')

        return cleaned_data

    def save(self, commit=True):
        admin = super().save(commit=False)
        if commit:
            admin.save()
            user = User.objects.create_user(
                username=self.cleaned_data['email'],
                email=self.cleaned_data['email'],
                password=self.cleaned_data['password'],
            )
            user.is_staff = True
            user.save()
        return admin
