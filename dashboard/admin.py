from django.contrib import admin
from .models import UserDetails, CandidateDetails, Subscription

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(CandidateDetails)
admin.site.register(Subscription)
