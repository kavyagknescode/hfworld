from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views

# Create your views here.

def CustomLoginView(request, **kwargs):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        return auth_views.login(request, **kwargs)
