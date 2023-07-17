from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main_page'),
    path('top-sellers', topSellers, name='top-sellers'),
    path('login', login, name='login'),
]



