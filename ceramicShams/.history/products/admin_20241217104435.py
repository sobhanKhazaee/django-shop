from django.contrib import admin
from . import models
# Register your models here.


class productAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }
    list_display = ('name', 'price', 'rate', 'is_active',)
    list_editable = [ 'is_active',]

class categoryAdmin(admin.ModelAdmin):

admin.site.register(models.Category, categoryAdmin)
admin.site.register(models.Product, productAdmin)

