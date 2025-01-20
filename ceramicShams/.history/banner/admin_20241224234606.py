from django.contrib import admin
from .models import Banner


class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'active', 'created_at')
    list_filter = ('position', 'active', 'created_at')
    search_fields = ('title', 'description')
admin.site.register()