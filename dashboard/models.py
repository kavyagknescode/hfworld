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
    inv_pin = models.IntegerField(verbose_name="Invoice Pin", blank=True)

    del_address = models.CharField(verbose_name="Delivery Address", max_length=255, blank=True)
    del_city = models.CharField(verbose_name="Delivery City", max_length=100, blank=True)
    del_state = models.CharField(verbose_name="Delivery State", max_length=100, blank=True)
    del_pin = models.IntegerField(verbose_name="Delivery Pin", blank=True)

    def __str__(self):
        return (self.user_uname)
