from django.contrib import admin
from . import models

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display =["username","email","is_active"]
    list_editable = ["is_active"]

admin.site.register(models.User,UserAdmin)