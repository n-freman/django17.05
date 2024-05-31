from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.add_message(
                request,
                messages.ERROR,
                'Такой пользователь уже есть'
            )
            return redirect('register')
        user = User(username=username)
        user.set_password(password)
        user.save()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Successfully registered. Please login now'
        )
        return redirect('login')
    return render(request, 'custom_auth/register.html')


def login_page(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.add_message(
                request,
                messages.ERROR,
                'Username or password was wrong'
            )
            return redirect('login')
        login(request, user)
        messages.add_message(
            request,
            messages.SUCCESS,
            'Successfully logged in'
        )
        return redirect('home')
    return render(request, 'custom_auth/login.html')


def logout_view(request):
    logout(request)
    messages.add_message(
        request,
        messages.INFO,
        'Logged out'
    )
    return redirect('home')
