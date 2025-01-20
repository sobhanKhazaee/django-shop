from django.contrib import admin
from . import models
from jalali_date import datetime2jalali
from utils.helpers import show_jalali_date
# Register your models here.


class ArticelCommentsAdmin(admin.ModelAdmin):
    list_display = ["user", "article", "get_created_jalali"]
    list_filter = [ar]
    def get_created_jalali(self, obj):
        date = show_jalali_date(obj.created_at)
        time = datetime2jalali(obj.created_at).strftime(' %H:%M:%S')       
        return f"{date} - {time}"
    get_created_jalali.short_description = "تاریخ ثبت نظر"


admin.site.register(models.Aticel)
admin.site.register(models.ArticelCategories)
admin.site.register(models.ArticelComments, ArticelCommentsAdmin)
