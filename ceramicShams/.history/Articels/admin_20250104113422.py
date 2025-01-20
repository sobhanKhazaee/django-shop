from django.contrib import admin
from . import models
from jalali_date import datetime2jalali

# Register your models here.


class ArticelCommentsAdmin(admin.ModelAdmin):
    list_display = ["user", "article", "get_created_jalali"]

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%Y%m% %H:%M:%S')


admin.site.register(models.Aticel)
admin.site.register(models.ArticelCategories)
admin.site.register(models.ArticelComments, ArticelCommentsAdmin)
