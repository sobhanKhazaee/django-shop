from django.contrib import admin
from .models import Category,Product,ProductTags,Brand
from django.http import HttpRequest
# Register your models here.


class productAdmin(admin.ModelAdmin):
    list_display = ["name","price","is_active"]
    list_editable = ["price","is_active"]
    
    def save_model(self, request:HttpRequest, obj:Product, form, change):
        if change:
            obj.slug = request.name
        return super().save_model(request, obj, form, change)




admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductTags)
admin.site.register(Brand)
