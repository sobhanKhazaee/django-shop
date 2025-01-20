from django.db import models
from account.models import 

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey()