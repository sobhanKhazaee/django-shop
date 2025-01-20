from django.contrib import admin
from . import models

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display =["username","is_active"]

admin.site.register(models.User,UserAdmin)