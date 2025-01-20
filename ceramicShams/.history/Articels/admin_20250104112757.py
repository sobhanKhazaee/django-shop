from django.contrib import admin
from . import models
from jalali_date import date2jalali

# Register your models here.


class ArticelCommentsAdmin(admin.ModelAdmin):
    list_display = ["user", "article", "created_at"]

def get_created_jalali(self, obj):
		return datetime2jalali(obj.created).strftime('%a, %d %b %Y %H:%M:%S')



admin.site.register(models.Aticel)
admin.site.register(models.ArticelCategories)
admin.site.register(models.ArticelComments, ArticelCommentsAdmin)
