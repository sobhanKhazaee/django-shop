from django.contrib import admin
from . import models

class SiteSettingAdmin(models.M)

# Register your models here.
admin.site.register(models.SiteSetting)
admin.site.register(models.LinkCategory)
admin.site.register(models.FooterLinks)
