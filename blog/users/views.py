from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('posts:news')
        else:
            messages.info(request, 'Try again! username or password is incorrect')

    context = {}
    return render(request, 'users/login.html', context)

def home_page(request):
    return render(request, 'users/homepage.html')

def logout_page(request):
    logout(request)
    return redirect('users:login')

def register_page(request):
    if request.method != 'POST':
        form = CustomUserForm()
    else:
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')

    context = {'form': form}

    return render(request, 'users/register.html', context)
