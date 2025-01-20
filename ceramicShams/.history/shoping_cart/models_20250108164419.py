from django.db import models
from account.models import UserI

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE)