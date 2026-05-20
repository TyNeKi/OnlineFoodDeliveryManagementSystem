from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index_view(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        login_input = request.POST.get('email')
        password = request.POST.get('password')
        
        user = None
        # Check if the input is an email or a username
        if '@' in login_input:
            try:
                # Find the user by their email
                user_record = User.objects.get(email=login_input)
                # Authenticate using the found username
                user = authenticate(request, username=user_record.username, password=password)
            except User.DoesNotExist:
                # No user has this email address
                pass # Will be handled by the final 'if user is None' check
        else:
            # Assume it's a username and authenticate directly
            user = authenticate(request, username=login_input, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('index')
        else:
            # If authentication fails for any reason, show a generic error
            messages.error(request, 'Invalid credentials. Please check your username/email and password.')
            return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')
            
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'register.html')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('index')

    return render(request, 'register.html')

@login_required(login_url='/login/')
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        
        new_email = request.POST.get('email', '')
        if new_email and new_email != user.email:
            if User.objects.filter(email=new_email).exists():
                messages.error(request, 'Email is already in use.')
                return redirect('profile')
            user.email = new_email
            
        user.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('profile')
        
    return render(request, 'profile.html')

@login_required(login_url='/login/')
def add_record_view(request):
    # Redirect to a concrete add view based on requirements
    return redirect('add_new_restaurant')