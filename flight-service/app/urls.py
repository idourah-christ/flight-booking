from django.contrib import admin
from django.urls import path
from flight.views import index


urlpatterns = [
    
    path('', index)
]

