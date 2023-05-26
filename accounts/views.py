# account/views.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from . import forms


def login(request):
    if request.method == 'POST':
        form = forms.CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                django_login(request, user)  # Use Django's login function with the imported name
                return redirect('posts:index')
            else:
                form.add_error(None, '아이디와 비밀번호를 확인해 주세요')
    else:
        form = forms.CustomAuthenticationForm(request)

    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = forms.CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})