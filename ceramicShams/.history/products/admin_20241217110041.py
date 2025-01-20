from django.contrib import admin
from . import models
# Register your models here.


class productAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }
    list_display = ('name', 'price', 'rate', 'is_active',)
    list_editable = [ 'is_active',]
      def formatted_price(self, obj):
        return f"{obj.price:,}"  # نمایش قیمت با کاما
    formatted_price.short_description = "قیمت (فرمت‌شده)"

class categoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Category, categoryAdmin)
admin.site.register(models.Product, productAdmin)

