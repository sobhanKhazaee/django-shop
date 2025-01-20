from django.urls import path
from .  import

urlpatterns = [
      path('contact_us', views.contact_us, name='contact_us'),
]
