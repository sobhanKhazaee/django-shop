from django.contrib import admin
from . import models
from jalali_date import datetime2jalali

# Register your models here.


class ArticelCommentsAdmin(admin.ModelAdmin):
    list_display = ["user", "article", "get_created_jalali"]

    def get_created_jalali(self, obj):
        jalali_date = date2jalali(obj.created_at).strftime('%a, %d %b %Y')
        jalali_time = date2jalali(obj.created_at).strftime('%H:%M:%S')
        return f"{jalali_date}\n{jalali_time}"
    get_created_jalali.short_description = "تاریخ ثبت نظر"


admin.site.register(models.Aticel)
admin.site.register(models.ArticelCategories)
admin.site.register(models.ArticelComments, ArticelCommentsAdmin)
