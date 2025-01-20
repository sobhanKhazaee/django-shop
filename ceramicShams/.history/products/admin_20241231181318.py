from django.contrib import admin
from .models import Category,Product,ProductTags,Brand
from django.http import HttpRequest

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
    list_display = ["name","price","is_active","created_at"]
    list_editable = ["price","is_active"]
    search_fields = ["name"]
    list_filter = ["rate","price"]
    





admin.site.register(Category)
admin.site.register(Product,productAdmin)
admin.site.register(ProductTags)
admin.site.register(Brand)
