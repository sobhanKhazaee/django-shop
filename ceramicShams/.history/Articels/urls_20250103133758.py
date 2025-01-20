from django.urls import path
from . import views

urlpatterns = [
     path('',views.ArticelsListView.as_view(),name="articels_view"),
     path('<str:category>',views.ArticelsListView.as_view(),name="articels_view_bycategory"),
     path('<slug:s>',views.ArticelDetailsView.as_view(),name="articel_details"),
     
]
