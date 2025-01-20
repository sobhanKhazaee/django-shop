from django.contrib import admin
from .models import Category,Product,ProductTags,Brand,ProductsVisit
from django import forms
from jalali_date.widgets import AdminJalaliDateWidget
from slugify import slugify
from utils.helpers import show_jalali_date
# Register your models here.

# class ProductAdminForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = "__all__"
#         widgets = {
#             'created_at': AdminJalaliDateWidget,  # ویجت تاریخ شمسی
#             'updated_at': AdminJalaliDateWidget,  # ویجت تاریخ شمسی
#         }
        


class productAdmin(admin.ModelAdmin):
    exclude = ['slug'] 
    list_display = ["name","price","is_active","get_jalali_create_date","visit_count"]
    list_editable = ["price","is_active"]
    search_fields = ["name"]
    list_filter = ["rate","price"]


    
    # def get_jalali_create_date(self, obj):
    #     return obj.get_jalali_create_date()
    # get_jalali_create_date.short_description = "تاریخ ایجاد (شمسی)"
     



admin.site.register(Product,productAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductTags)
# admin.site.register(ProductsVisit)