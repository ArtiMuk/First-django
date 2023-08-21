from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import AdvertisementForm
from .models import Advertisement
# Create your views here.
def index(request):
    adverts= Advertisement.objects.all()
    context = {'adverts': adverts}
    return render(request, 'app_adverts/index.html', context)

def topSellers(request):
    return render(request, 'app_adverts/top-sellers.html')

# def login(request):
#     return render(request, 'app_auth/login.html')

def advertPost(request):
    if request.method=='POST':
        form=AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.user = request.user
            advertisement.save()
            url=reverse('main_page')
            return redirect(url)
    else:
        form=AdvertisementForm()
    context={'form':form}
    return render(request, 'app_adverts/advertisement-post.html', context)
    
    