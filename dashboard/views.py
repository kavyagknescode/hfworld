from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from dashboard.models import UserDetails
from dashboard.forms import UserDetailsForm

# Create your views here.
def dash_view(request):
    check_user = UserDetails.objects.filter(user_uname=request.user) # checking if user has filled up details

    if check_user:
        print('has data')
        user_data = UserDetails.objects.get(user_uname=request.user)
        return render(request, 'dashboard/user_dash.html',{'user_data':user_data,})

    else:
        print('no data')
        form = UserDetailsForm()
        return render(request, 'dashboard/add_profile.html', {'form':form})

def save_user_details(request,pk):
    # form = UserDetailsForm()
    # return render(request, 'dashboard/add_profile.html', {'form':form})

    if request.method == 'POST':
        print('post method')
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            print('valid form')
            user_dtls = form.save(commit=False)
            user_dtls.user_uname = request.user
            user_dtls.email = request.user.email
            user_dtls.save()
            return redirect('dashboard:user-dashboard')
        else:
            print('invalid form')
            print (form.errors)
            form = UserDetailsForm()
            return render(request, 'dashboard/add_profile.html', {'form':form})
    else:
        print('non post method')
        form = UserDetailsForm()
        return render(request, 'dashboard/add_profile.html', {'form':form})
