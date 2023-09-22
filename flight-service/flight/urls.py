from django.urls import path, include
from .views import index


app_name = "flight"

urlpatterns = [
    path('/', index),
]
