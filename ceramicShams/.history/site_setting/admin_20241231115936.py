from django.contrib import admin
from . import models

class SiteSettingAdmin(admin.ModelAdmin):
    def has_add_permission (self,request):
        if models.SiteSetting.objects.exists():
            return False
        return True

class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ["link_title","cat","li"]


# Register your models here.
admin.site.register(models.SiteSetting,SiteSettingAdmin)
admin.site.register(models.LinkCategory)
admin.site.register(models.FooterLinks,FooterLinkAdmin)
admin.site.register(models.SocialMedia)
