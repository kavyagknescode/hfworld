from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from dashboard.models import UserDetails, CandidateDetails, Subscription
from .models import UserSubscription

import razorpay

#kuntal.karmakar19@gmail.com account
client = razorpay.Client(auth=("rzp_test_0bogBh0wb4NS1C", "AioV8HdqfiSWWbUepUjj9BL2"))
paid = client.payment.all()

# Create your views here.
def subscription_view(request):
    subscriptions = Subscription.objects.all()
    return render(request, 'subscription/user_show_subscription.html', {'subscriptions':subscriptions})

@login_required
def buy_subscription(request,amt):
    user = UserDetails.objects.get(user_uname=request.user)
    # Converting to Paise for Razorpay
    amt = amt*100
    return render(request, 'subscription/payment.html',{'user':user, 'amt':amt,})

def view_candidates(request):
    """
    If user is not paid
    redirect to buy subscription page
    """
    if paid['count'] == 0:
        print('no transaction')
        subscriptions = Subscription.objects.all()
        return render(request, 'subscription/user_show_subscription.html', {'subscriptions':subscriptions})

    else:
        print('has transaction')
        for num in range(0,paid['count']):
            print('already paid')
            """
            For paid users
            """
            if paid['items'][num]['email'] == request.user.email and paid['items'][num]['status'] == 'authorized':
                print(request.user.email)
                # print(client.payment.fetch(paid['items'][num]['id']))
                # # Capture amount in paise
                # if paid['items'][num]['captured'] == False :
                #     client.payment.capture(paid['items'][num]['id'], "20000")
                # else:
                #     continue
                user_sub = UserSubscription(user_uname=request.user, sub_pack=paid['items'][num]['amount'])
                user_sub.save()

                candidates = CandidateDetails.objects.all()
                return render(request, 'subscription/candidates.html', {'candidates':candidates})

            else:
                """
                If payment is not successful
                """
                print('no payment')
                return redirect('subscription:subscription-view')

def SubscribedPack(request):
    l1 = []
    for num in range(0,paid['count']):
        if paid['items'][num]['email']==request.user.email and paid['items'][num]['status']=='authorized':
            print(paid)
            sub_pack = l1.append()
            print(l1)
    return render(request, 'dashboard/dashboard.html', {'packs':l1})

def payment_thanks(request):
    return render(request, 'subscription/payment_thanks.html')
