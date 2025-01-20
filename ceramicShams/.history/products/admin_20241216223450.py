from django.contrib import admin
from . import models
# Register your models here.


class productAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }
    list_display=('price','rate','is_active',)

admin.site.register(models.Product, productAdmin)
