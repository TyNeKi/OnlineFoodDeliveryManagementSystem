from django import forms
from .models import Restaurant, Category, Menu, MenuItem

class RestaurantForm(forms.ModelForm):
    openingTime = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    closingTime = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Restaurant
        exclude = ('userID',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'
