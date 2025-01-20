from django.urls import path
from . import views

urlpatterns = [
     path('',views.ArticelsListView.as_view(),name="articels_view"),
     path('<str:category>',views.ArticelsListView.as_view(),name="articels_view_bycategory"),
     path('<pk>',views.ArticelsListView.as_view(),name="articels_view_bycategory"),
     
]
