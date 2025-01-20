from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.productsListView.as_view(), name='all_products'),
    path('<slug:slug >', views.productDetailsView.as_view(), name='productDetails'),
    path('sort-by-cat/<int:cat_id>/',
         views.sortByCatView.as_view(), name='sort_by_cat'),
    path('sortByTag/<tag>/', views.SortByTagView.as_view(), name='sortByTag'),
]
