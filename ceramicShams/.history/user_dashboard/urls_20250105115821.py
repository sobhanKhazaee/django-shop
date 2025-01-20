from django.urls import path

urlpatterns = [
    path('', views.dashboard, name='dashboard_page'),
]

