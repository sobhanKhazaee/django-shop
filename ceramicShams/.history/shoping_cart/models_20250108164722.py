from django.db import models
from account.models import User
from django.db.models import CASCADE


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE,verbose_name="کاربر")
    payment = models.BooleanField(default=False,verbose_name="پرداخت شده / نشده")
    payment_date = models.DateTimeField(null)