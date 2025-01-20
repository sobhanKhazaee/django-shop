from django.contrib import admin
from . import models
# Register your models here.
class productAdmin(admin.ModelAdmin):
    prp


admin.site.register(models.Product,productAdmin)
