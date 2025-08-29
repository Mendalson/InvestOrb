from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms


def main_view(request):
    return render(request, 'main_page.html')


def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users:main')
    else:
        form = forms.LoginForm()
    return render(request, 'login_page.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:main')
    else:
        form = forms.RegisterForm()
    return render(request, 'register_page.html', {'form': form})
