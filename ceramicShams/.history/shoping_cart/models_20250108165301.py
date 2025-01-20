from django.db import models
from account.models import User
from products.models import Product
from django.db.models import CASCADE


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE,verbose_name="کاربر")
    payment = models.BooleanField(default=False,verbose_name="پرداخت شده / نشده")
    payment_date = models.DateTimeField(null=True,blank=True,verbose_name="تاریخ پراخت")
    
class Order(models.Model):
    cart = models.ForeignKey(Cart,on_delete=CASCADE,verbose_name="سبد خرید")
    count = models.IntegerField(verbose_name="تعداد")
    product = models.ForeignKey(Product,on_delete=CASCADE,verbose_name=)