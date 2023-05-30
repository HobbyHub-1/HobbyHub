# account/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from .forms import CustomAuthenticationForm, CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('posts:index')
            else:
                form.add_error(None, '아이디와 비밀번호를 확인해 주세요')
    else:
        form = CustomAuthenticationForm(request)

    return render(request, 'accounts/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('posts:index')


def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('accounts:profile', request.user)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/password.html', context)

@login_required
def delete(request, username):
    person = get_user_model().objects.get(username=username)
    if request.user == person:
        person.delete()
        auth_logout(request)
        
    return redirect('posts:index')