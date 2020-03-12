from django.shortcuts import render, redirect

# Create your views here.
def dash_view(request):
    return render(request, 'dashboard/add_profile.html',)
