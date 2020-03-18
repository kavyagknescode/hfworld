from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserSubscription(models.Model):
    """
    It stores the User's subscriptions bought
    """
    user_uname = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='User Name')
    sub_pack = models.IntegerField('Subscription Pack', blank=True, null=True, default=0)

    # def __str__(self):
    #     if self.user_uname==None:
    #         return "ERROR-CUSTOMER NAME IS NULL"
    #     return self.user_uname
