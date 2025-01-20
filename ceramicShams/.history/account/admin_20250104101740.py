from django.contrib import admin
from . import models

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display =["username","email","is_active","is_staff"]
    list_editable = ["is_active","is_staff"]
    search_fields = ["email",]

admin.site.register(models.User,UserAdmin)