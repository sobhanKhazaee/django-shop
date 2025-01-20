from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('manage_pages.urls')),
    path('products/', include('products.urls')),
    path('articels/', include('Articels.urls')),
    path('contact-us/', include('contactUs.urls')),
    path('register/', include('account.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
