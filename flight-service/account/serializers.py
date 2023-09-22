from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model 
from .models import UserAccount as User
from django.core.exceptions import ValidationError

User = get_user_model() 

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('email','last_name','first_name','phone','password')


class ValidEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class OTPCodeEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()


