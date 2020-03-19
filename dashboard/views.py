from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from dashboard.models import UserDetails, CandidateDetails
from dashboard.forms import UserDetailsForm, CandidateDetailsForm

import razorpay

#kuntal.karmakar19@gmail.com account
client = razorpay.Client(auth=("rzp_test_0bogBh0wb4NS1C", "AioV8HdqfiSWWbUepUjj9BL2"))
paid = client.payment.all()

# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

def dashboard(request):
    if request.user.is_superuser:
        return render(request, 'dashboard/admin_dash.html')
    else:
        l1 = []
        for num in range(0,paid['count']):
            if paid['items'][num]['email']==request.user.email and paid['items'][num]['status']=='authorized':
                amount = paid['items'][num]['amount'] / 100
                l1.append(amount)
        return render(request, 'dashboard/dashboard.html', {'packs':l1})

def profile_view(request):
    check_user = UserDetails.objects.filter(user_uname=request.user) # checking if user has filled up details

    if check_user:
        print('has data')
        user_data = UserDetails.objects.get(user_uname=request.user)
        return render(request, 'dashboard/user_profile.html',{'user_data':user_data,})

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

def edit_user_details(request,id):
    user_data = UserDetails.objects.get(id=id)
    return render(request, 'dashboard/edit_profile.html', {'user_data':user_data})

def save_edited_details(request,id):
    new_data = UserDetails.objects.get(id=id)
    if request.method == 'POST':
        new_data.user_uname = request.user
        new_data.first_name = request.POST['fname']
        new_data.last_name = request.POST['lname']
        new_data.email = request.POST['email']
        new_data.phone = request.POST['phone']

        try:
            validate_email(new_data.email)
        except ValidationError:
            messages.error(request, "Enter a Valid Email")

        new_data.save()
        return redirect('dashboard:user-dashboard')
    else:
        return redirect('dashboard:user-dashboard')

def add_candidate_view(request):
    form = CandidateDetailsForm()

    if request.method == 'POST':
        print('Post Method')
        form = CandidateDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            print('Valid form')
            candidate = form.save(commit=False)
            candidate.save()
            return redirect('dashboard:show-candidate')

        else:
            print(form.errors)
            return render(request, 'dashboard/add_candidate.html', {'form':form})

    else:
        return render(request, 'dashboard/add_candidate.html', {'form':form})

def show_candidate_view(request):
    candidates = CandidateDetails.objects.all()
    return render(request, 'dashboard/show_candidate.html', {'candidates':candidates})
