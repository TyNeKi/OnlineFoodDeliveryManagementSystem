from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def index_view(request):
    return render(request, 'index.html')


@login_required
def home_view(request):
    return render(request, 'home.html')


@login_required
def edit_profile_view(request):
    user = request.user
    if request.method == 'POST':
        new_username = request.POST.get('username', '').strip()
        new_password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        if not new_username:
            messages.error(request, 'Username is required.')
        elif User.objects.filter(username=new_username).exclude(pk=user.pk).exists():
            messages.error(request, 'That username is already taken.')
        elif not new_password:
            messages.error(request, 'Password is required.')
        elif new_password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        else:
            user.username = new_username
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Profile updated successfully! Please log in again with your new credentials.')
            return redirect('login')

    return render(request, 'edit_profile.html', {'user': user})


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
            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('home')
        else:
            messages.error(request, 'Invalid login details. Please try again.')

    return render(request, 'login.html')


@login_required
def add_user_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        email = request.POST.get('email', '').strip()

        if not username or not password:
            messages.error(request, 'Username and password are required.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'That username is already taken.')
        else:
            User.objects.create_user(username=username, password=password, email=email)
            messages.success(request, f'User {username} created successfully.')
            return redirect('add_user')

    return render(request, 'add_user.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')