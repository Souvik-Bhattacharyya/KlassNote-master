from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout
from django.contrib.auth.views import login_required


def login_view(request):
    if request.method == 'POST':
        pass
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        pass
    return render(request, 'register.html')


def verify_view(request):
    if request.method == 'POST':
        pass
    return render(request, 'verify.html')


def forgot_view(request):
    if request.method == 'POST':
        pass
    return render(request, 'forgot.html')


def reset_view(request):
    if request.method == 'POST':
        pass
    return render(request, 'reset.html')
