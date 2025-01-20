from django.contrib import admin
from .models import Category,Product,ProductTags,Brand
from django.http import HttpRequest
from django import forms
from jalali_date.widgets import AdminJalaliDateWidget
from jalali_date.admin import ModelAdminJalaliMixin
from slugify import slugify

# Register your models here.

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            'created_at': AdminJalaliDateWidget,  # ویجت تاریخ شمسی
            'updated_at': AdminJalaliDateWidget,  # ویجت تاریخ شمسی
        }

class productAdmin(admin.ModelAdmin):
    list_display = ["name","price","is_active","get_jalali_create_date"]
    list_editable = ["price","is_active"]
    search_fields = ["name"]
    list_filter = ["rate","price"]
    def save_model(self, request, obj:, form, change):
        if obj.
        return super().save_model(request, obj, form, change)

    
    def get_jalali_create_date(self, obj):
        return obj.get_jalali_create_date()
    get_jalali_create_date.short_description = "تاریخ ایجاد (شمسی)"





admin.site.register(Category)
admin.site.register(Product,productAdmin)
admin.site.register(ProductTags)
admin.site.register(Brand)
