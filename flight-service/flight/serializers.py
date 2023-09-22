from dataclasses import fields
from base.serializers import BaseModelSerializer
from rest_framework import serializers
from base.models import BaseModel

from .models import Flight, Booking, Airport

from rest_framework import serializers


class AirportSerializer(serializers.Serializer):
    name = serializers.CharField()

class AirportListSerializer(serializers.ListSerializer):
    child = AirportSerializer()

    def to_representation(self, data):
        return [AirportSerializer(item).data for item in data]






    