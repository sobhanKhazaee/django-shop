from django.urls import path
from . import views

urlpatterns = [
     path('',views.ArticelsListView.as_view(),name="articels_view"),
     path('<str:category>',views.ArticelsListView.as_view(),name="articels_view_bycategory"),
     path('detail/<int:pk>',views.ArticelDetailsView.as_view(),name="articel_details"),
      path('submit_comment/', views.submit_comment, name='submit_comment'),
     
]
