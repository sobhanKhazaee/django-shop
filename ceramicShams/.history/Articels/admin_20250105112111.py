from django.contrib import admin
from . import models
from jalali_date import datetime2jalali
from utils.helpers import show_jalali_date
from django import forms
from ckeditor.widgets import CKEditorWidget
# Register your models here.


class ArticleAdminForm(forms.ModelForm):
    بع = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ["title", "author", "get_created_jalali"]
    list_filter = ["author"]
    search_fields = ['title']

    def get_created_jalali(self, obj):
        date = show_jalali_date(obj.created_at)
        time = datetime2jalali(obj.created_at).strftime(' %H:%M:%S')       
        return f"{date} - {time}"
    get_created_jalali.short_description = "تاریخ ثبت مقاله"
#نظرات
class ArticelCommentsAdmin(admin.ModelAdmin):
    list_display = ["user", "article", "get_created_jalali"]
    list_filter = ["article"]
    search_fields = ['article__title']

    def get_created_jalali(self, obj):
        date = show_jalali_date(obj.created_at)
        time = datetime2jalali(obj.created_at).strftime(' %H:%M:%S')
        return f"{date} - {time}"
    get_created_jalali.short_description = "تاریخ ثبت نظر"


admin.site.register(models.Aticel,ArticleAdmin)
admin.site.register(models.ArticelCategories)
admin.site.register(models.ArticelComments, ArticelCommentsAdmin)
