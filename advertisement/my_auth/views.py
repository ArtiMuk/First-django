from django.shortcuts import render,reverse, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import User_creationForm

# def profile_view(request):
#     return render(request, 'app_auth/login.html')


def reg_view(request):
    if request.method== 'POST':
        form=User_creationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('prof'))
    else:
        form=User_creationForm()
        
    context={'form':form}
    return render(request, 'app_auth/register.html', context)

@login_required(login_url=reverse_lazy('log'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')


def login_view(request):
    redirect_url=reverse('prof')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
           return render(request, 'app_auth/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html', {'error':'Пользователь не авторизован'})
        
  

def logout_view(request):
    logout(request)
    return redirect(reverse('log'))