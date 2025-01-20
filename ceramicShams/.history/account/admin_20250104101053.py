from django.contrib import admin
from . import models

# Register your models here.
class UserAdmin(admin)

admin.site.register(models.User)