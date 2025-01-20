from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    # path('', views.productsList,name='home'),
    path('', views.productsListView.as_view(), name='all_products'),
    # i used re_path becaus i want make a custom slug with regular expressins
    re_path(r'^(?P<slug>[-\w\u0600-\u06FF]+)/$',
            views.productDetailsView.as_view(), name='productDetails'),
    path('sort-by-cat/<int:cat_id>/',vie, name='sort_by_cat'),
    path('sortByTag/<tag>/', views.sortByTag, name='sortByTag'),

]
