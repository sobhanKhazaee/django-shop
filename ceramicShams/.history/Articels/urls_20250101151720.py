from django.urls import path
from . import views

urlpatterns = [
     path('',views.ArticelsListView.as_view(),name="articels_view"),
     path('<catego>',views.ArticelsListView.as_view(),name="articels_view"),
]
