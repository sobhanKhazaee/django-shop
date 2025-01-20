from django.contrib import admin
from . import models
# Register your models here.


class productAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }
    list_display = ('name', 'formatted_price', 'rate', 'is_active',)
    list_editable = ['is_active',]




admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.ProductTags)
admin.site.register(models.Brand)
