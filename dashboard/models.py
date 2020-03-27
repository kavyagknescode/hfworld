from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

# Create your models here.
class UserDetails(models.Model):
    user_uname = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    first_name = models.CharField('First Name', max_length=255, blank=True)
    last_name = models.CharField('Last Name', max_length=255, blank=True)
    phone = models.CharField('Phone Number', max_length=12, blank=True)
    email = models.EmailField()

    inv_address = models.CharField(verbose_name="Invoice Address", max_length=255, blank=True)
    inv_city = models.CharField(verbose_name="Invoice City", max_length=100, blank=True)
    inv_state = models.CharField(verbose_name="Invoice State", max_length=100, blank=True)
    inv_pin = models.IntegerField(verbose_name="Invoice Pin", blank=True,)

    del_address = models.CharField(verbose_name="Delivery Address", max_length=255, blank=True)
    del_city = models.CharField(verbose_name="Delivery City", max_length=100, blank=True)
    del_state = models.CharField(verbose_name="Delivery State", max_length=100, blank=True)
    del_pin = models.IntegerField(verbose_name="Delivery Pin", blank=True)

    def __str__(self):
        return (self.first_name)

    class Meta:
        verbose_name_plural = 'UserDetails'


class CandidateDetails(models.Model):
    name = models.CharField('Full Name', max_length=255)
    degree = models.CharField('Degree', max_length=255, blank=True)
    stream = models.CharField('Stream', max_length=255, blank=True)
    location = models.CharField('Current Location of the Candidate', max_length=255, blank=True)
    resume = models.FileField(upload_to = 'candidate/%Y/%m/', help_text="Upload PDF File Only")
    date_added = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'CandidateDetails'

class Subscription(models.Model):
    """
    Add Subscription Pack by Admin
    """
    pack_name = models.CharField('Subscription Name', max_length=255)
    price = models.PositiveIntegerField('Subscription Price',)
    no_resume = models.IntegerField('No. of Resume User can Access')

    def __str__(self):
        return self.pack_name
