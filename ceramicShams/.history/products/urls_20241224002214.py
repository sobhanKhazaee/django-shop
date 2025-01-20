from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    # path('', views.productsList,name='home'),
    path('', views.productsListView.as_view(),name='all'),
    # i used re_path becaus i want make a custom slug with regular expressins
    re_path(r'^(?P<slug>[-\w\u0600-\u06FF]+)/$',
            views.productDetails, name='productDetails'),
    path('sortByCat/<int:cat_id>/', views.sortByCat, name='sortByCat'),
    path('sortByTag/<tag>/', views.sortByTag, name='sortByTag'),
  
]
