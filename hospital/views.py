from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно прошли регистрацию')
            return redirect('/')
        else:
            messages.success(request, 'Что то пошло не так')
    else:
        form = UserCreationForm()
    return render(request, 'hospital/register.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Успех')
            return redirect('/')
        else:
            messages.error(request, 'Неудача')
    else:
        form = UserLoginForm()
    return render(request, 'hospital/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('/')
def index(request):
    return render(request, 'hospital/index.html')
