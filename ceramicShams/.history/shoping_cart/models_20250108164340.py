from django.db import models
from account.mo

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey()