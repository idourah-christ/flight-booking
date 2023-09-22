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

      
@api_view(['POST'])
def booking(request):
    post_data = request.data
    flight_name = post_data.get("flight", None)
    date = post_data.get("date", None)
    
    if flight_name == None:
        return Response({"message":"Missing fields"},status=status.HTTP_400_BAD_REQUEST)

    booking = {"flight":flight_name, "date":date}
    bookings.append(booking)
    return Response({"message":"Booking success"},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_currency_view(request):
    currencies = {"data":get_currency(currency_path)}
    return Response(currencies)

        



    
