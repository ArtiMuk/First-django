from django.shortcuts import render,reverse, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def profile_view(request):
    return render(request, 'app_auth/login.html')


def reg_view(request):
    return render(request, 'app_auth/register.html')

@login_required(login_url=reverse_lazy('log'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')


def login_view(request):
    redirect_url=reverse('prof')
    if request.method == 'GET':
        if request.user.is_authenticated:
            print('hi')
            return redirect(redirect_url)
        else:
            print('bye')
            return render(request, 'app_auth/login.html')
    
    username = request.POST('Username')
    password = request.POST('Password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {'error':'Пользователь не авторизован'})

def logout_view(request):
    logout(request)
    return redirect(reverse('log'))