from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import AdminForm, RegisterForm, UserProfileForm

def index_view(request):
    return render(request, 'accounts/index.html')


def add_admin_view(request):
    form = AdminForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'accounts/addNewAdmin.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        # Grab whatever they typed into the first box
        login_input = request.POST.get('email')
        password = request.POST.get('password')

        # NEW LOGIC: Check if they typed an email or a username
        if '@' in login_input:
            try:
                user_record = User.objects.get(email=login_input)
                username_to_check = user_record.username
            except User.DoesNotExist:
                username_to_check = None
        else:
            # If there's no '@', assume they just typed their Superuser username!
            username_to_check = login_input

        # Verify the password
        user = authenticate(request, username=username_to_check, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login details. Please try again.')

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})


@login_required(login_url='login')
def home_view(request):
    user = request.user
    context = {
        'user': user,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    }
    return render(request, 'home.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


@login_required(login_url='login')
def edit_profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Error updating profile. Please try again.')
    else:
        form = UserProfileForm(instance=user)
    
    return render(request, 'edit_profile.html', {'form': form})