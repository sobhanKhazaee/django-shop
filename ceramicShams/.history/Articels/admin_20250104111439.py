from django.contrib import admin
from . import models

# Register your models here.

class ArticelCommentsAdmin(admin.ModelAdmin):
    list_display = ["user","article"]

admin.site.register(models.Aticel)
admin.site.register(models.ArticelCategories)
admin.site.register(models.ArticelComments)