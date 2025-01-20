from django.contrib import admin
from . import models
# Register your models here.
class productAdmin(admin.ModelAdmin):
    prepopulated_fields={
        slug : []
    }


admin.site.register(models.Product,productAdmin)
