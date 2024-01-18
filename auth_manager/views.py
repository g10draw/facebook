from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import CustomUser
from .forms import RegistrationForm

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration Successful')
            messages.success(request, 'Login with your details')
            return redirect('login-page')
    else:
        form = RegistrationForm()
    return render(request, 'auth/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('timeline-page')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home-page')