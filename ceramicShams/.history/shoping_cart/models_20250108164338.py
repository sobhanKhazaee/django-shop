from django.db import models
from account.

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey()