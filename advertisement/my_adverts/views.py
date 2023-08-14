from django.shortcuts import render
from .models import Advertisement
# Create your views here.
def index(request):
    adverts= Advertisement.objects.all()
    context = {'adverts': adverts}
    return render(request, 'index.html', context)

def topSellers(request):
    return render(request, 'top-sellers.html')

def login(request):
    return render(request, 'login.html')