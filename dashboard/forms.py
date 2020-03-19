from django import forms
from django.forms import Textarea
from .models import UserDetails, CandidateDetails

# Model Form
class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        exclude = ('user_uname', 'email',)

class CandidateDetailsForm(forms.ModelForm):
    class Meta:
        model = CandidateDetails
        fields = ('name', 'degree', 'stream', 'location', 'resume',)
