from django.db import models
from account.models import User

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(U)