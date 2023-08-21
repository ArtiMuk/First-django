from django.urls import path
from .views import *

urlpatterns = [
    path('profile',profile_view, name='prof'),
    path('register',reg_view, name='reg'),
    path('logout',logout_view, name='logout'),
    path('login',login_view, name='log'),
]
