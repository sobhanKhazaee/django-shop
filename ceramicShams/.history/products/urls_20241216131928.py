from django.urls import path
from . import views

urlpatterns = [
    path('', views.productsList),
    path('<sl:product_id>', views.productDetails, name='productDetails')
]
