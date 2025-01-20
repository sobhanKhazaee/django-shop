from django.contrib import admin
from . import models
# Register your models here.


class productAdmin(admin.ModelAdmin):
    list_display = ["name","price","is_active","name"]




admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.ProductTags)
admin.site.register(models.Brand)
