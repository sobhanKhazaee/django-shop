from django.contrib import admin
from . import models
from jalali_date import datetime2jalali

# Register your models here.


class ArticelCommentsAdmin(admin.ModelAdmin):
    list_display = ["user", "article", "get_created_jalali"]

    def get_created_jalali(self, obj):
        date = datetime2jalali(obj.created_at).strftime('%Y%m%d')
        time = datetime2jalali(obj.created_at).strftime(' %H:%M:%S')       
        return f"{}"
    get_created_jalali.short_description = "تاریخ ثبت نظر"


admin.site.register(models.Aticel)
admin.site.register(models.ArticelCategories)
admin.site.register(models.ArticelComments, ArticelCommentsAdmin)
