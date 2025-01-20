from django.contrib import admin
from . import models
# Register your models here.
class productAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Product,productAdmin)
