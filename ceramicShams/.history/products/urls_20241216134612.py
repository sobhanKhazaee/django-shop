from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.productsList),
    re_path(r'^(?P<slug>[-\w\u0600-\u06FF]+)/$',
            views.productDetails, name='productDetails'),
]
