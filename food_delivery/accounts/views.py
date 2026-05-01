from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index_view(request):
    return render(request, 'index.html')


@login_required
def home_view(request):
    return render(request, 'home.html')


@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('home')

    return render(request, 'edit_profile.html')


def login_view(request):
    if request.method == 'POST':
        login_input = request.POST.get('email')
        password = request.POST.get('password')

        if '@' in login_input:
            try:
                user_record = User.objects.get(email=login_input)
                username_to_check = user_record.username
            except User.DoesNotExist:
                username_to_check = None
        else:
            username_to_check = login_input

        user = authenticate(request, username=username_to_check, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login details. Please try again.')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('index')