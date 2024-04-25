from django.urls import path
from . import views

urlpatterns = [
    path('storefront/hello', views.say_hello)
]
