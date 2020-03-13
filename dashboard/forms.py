from django import forms
from django.forms import Textarea
from .models import UserDetails

# Model Form
class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        exclude = ('user_uname', 'email',)
