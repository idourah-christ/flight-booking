from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, 
    TokenVerifyView
)

from flight.views import index, booking, get_currency_view


urlpatterns = [
    
    path('', index),
    path('api/booking', booking),
    path('api/currency/', get_currency_view),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),

    path('api-auth/', include('rest_framework.urls', namespace="api-auth")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

