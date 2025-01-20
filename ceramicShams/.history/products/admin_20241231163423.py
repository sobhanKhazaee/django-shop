from django.contrib import admin
from . import models
# Register your models here.


class productAdmin(admin.ModelAdmin):
    list_display = ["name","price","is_active"]
    list_editable = ["price","is_active"]
    
    def save_model(self, request, obj, form, change):
        if change:
            
        return super().save_model(request, obj, form, change)




admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.ProductTags)
admin.site.register(models.Brand)
