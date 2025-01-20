from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.productsListView.as_view(), name='all_products'),

    path('sortByTag/<tag>/', views.SortByTagView.as_view(), name='sortByTag'),

    path('filter-by-price/', views.FilterByPriceView.as_view(),
         name='filter_by_price'),
    re_path(r'^(?P<slug>[-\w\u0600-\u06FF]+)/$',
            views.productDetailsView.as_view(), name='productDetails'),
]
