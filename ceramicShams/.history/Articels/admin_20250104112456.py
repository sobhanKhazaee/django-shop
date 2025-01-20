from django.contrib import admin
from . import models
from jalali_date import date2jalali

# Register your models here.


class ArticelCommentsAdmin(admin.ModelAdmin):
    list_display = ["user", "article", "created_at"]

    def save_model(self, request, obj, form, change):
        obj.created_at = date2jalali(obj.created_at)
        return super().save_model(request, obj, form, change)



admin.site.register(models.Aticel)
admin.site.register(models.ArticelCategories)
admin.site.register(models.ArticelComments, ArticelCommentsAdmin)
