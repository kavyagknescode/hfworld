from django import forms
from django.forms import Textarea
from .models import UserDetails, CandidateDetails, Subscription

# Model Form
class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        exclude = ('user_uname', 'email',)

class CandidateDetailsForm(forms.ModelForm):
    class Meta:
        model = CandidateDetails
        fields = ('name', 'degree', 'stream', 'location', 'resume',)
        exclude = ('date_added',)

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('pack_name', 'price', 'no_resume')
