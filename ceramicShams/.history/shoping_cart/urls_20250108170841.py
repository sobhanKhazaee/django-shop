from django.urls import path
from . import views

urlpatterns = [
    
   path('add-to-cart/', views.a, name='your_view_name'),
]