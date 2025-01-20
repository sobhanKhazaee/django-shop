from django.urls import path
from . import views

urlpatterns = [
    path('', views.productsList),
    path( گ , views.productDetails)
]
