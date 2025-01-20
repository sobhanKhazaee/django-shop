from django.contrib import admin
from . import models
# Register your models here.


class productAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }
    list_display = ('name', 'price', 'rate', 'is_active',)
    list_editable = []'name', 'price', 'rate', 'is_active',]


admin.site.register(models.Product, productAdmin)
