from django.contrib import admin
from . import models
from jalali_date import date2jalali

# Register your models here.


class ArticelCommentsAdmin(admin.ModelAdmin):
    list_display = ["user", "article","created_at"]
    
    def save_model(self, request, obj, form, change):
        
        return super().save_model(request, obj, form, change)
    # def show_jalali_date(created_at):
    # date = date2jalali(created_at).strftime(' %y/%m/%d ')
    # return english_to_persian(date)


admin.site.register(models.Aticel)
admin.site.register(models.ArticelCategories)
admin.site.register(models.ArticelComments, ArticelCommentsAdmin)
