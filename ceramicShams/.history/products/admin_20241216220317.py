from django.contrib import admin
from . import models
# Register your models here.
class productAdmin(admin.ModelAdmin):
    

admin.site.register(models.Product)
