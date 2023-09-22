from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .utils import get_currency
import requests


currency_url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"
currency_path = "flight/currency.xml"

bookings = []
data_service_url = "http://localhost:8002/flight"

# Create your views here.
@api_view(['GET'])
def index(request):
    try:
        response = requests.get(data_service_url)

        if response.status_code != 200:
            return Response({"message":"Error fetching flight", "status":response.status_code})
        
        flights = response.json()
        currencies = get_currency(currency_path)

        data = {
            "flights":flights,
            "currencies":currencies
        }
        return Response(data)
    
    except requests.exceptions:
        return Response({"message":"Error fetching flight"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        



    
