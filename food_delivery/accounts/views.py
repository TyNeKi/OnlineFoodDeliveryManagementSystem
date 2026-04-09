from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def index_view(request):
    return render(request, 'index.html')

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
            return redirect('index')
        else:
            messages.error(request, 'Invalid login details. Please try again.')

    # Notice the parenthesis is fixed here!
    return render(request, 'login.html')