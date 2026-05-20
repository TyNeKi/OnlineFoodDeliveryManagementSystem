from django.shortcuts import render, redirect
from .forms import RestaurantForm, CategoryForm, MenuForm, MenuItemForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'restaurant_index.html')

@login_required
def add_new_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.userID = request.user
            restaurant.save()
            messages.success(request, 'Restaurant added successfully!')
            return redirect('restaurant_index')
    else:
        form = RestaurantForm()
    return render(request, 'addNewRestaurant.html', {'form': form})

def add_new_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_index')
    else:
        form = CategoryForm()
    return render(request, 'addNewCategory.html', {'form': form})

def add_new_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_index')
    else:
        form = MenuForm()
    return render(request, 'addNewMenu.html', {'form': form})

def add_new_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_index')
    else:
        form = MenuItemForm()
    return render(request, 'addNewMenuItem.html', {'form': form})
