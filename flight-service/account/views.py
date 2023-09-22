# from django.shortcuts import render
# # Create your views here.
# from rest_framework.views import APIView
# from .models import UserAccount
# from .serializers import ValidEmailSerializer, OTPCodeEmailSerializer
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.parsers import MultiPartParser,  FormParser
# import logging
# from utils.otp.generator import generate_otp, verify_otp, generate_verification_code
# from rest_framework import serializers


# logger = logging.getLogger(__name__)


# class OTPAuthenticationView(APIView):
#     serializer_class = OTPCodeEmailSerializer
#     queryset = UserAccount.objects.all()

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)

#         try:
#             serializer.is_valid(raise_exception=True)
#         except serializers.ValidationError:
#             return Response({"message":"missing code or email in data"},status=status.HTTP_400_BAD_REQUEST)
       
#         email = serializer.validated_data.get("email")
#         try:
#             account = self.queryset.get(email=email)

#         except UserAccount.DoesNotExist:
#             return Response({"message":"User account not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         except Exception as e:
#             logger.error(f"Error retreiving email: {str(e)}")
#             return Response({"message":"Internal server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
          
#         code = serializer.validated_data.get("code")
        
#         if not account.code == code :
#             return Response({"message":"Invalid code {0}".format(code)}, status=status.HTTP_401_UNAUTHORIZED)
        
#         try:
#             account.is_active = True
#             account.save()
#         except Exception as e:
#             logger.error(f"Error updating user account is_active: {str(e)}")
#             return Response({"message":"Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#         return Response({"message":"authentification OTP reussie"},status=status.HTTP_200_OK)


# class SendOTPCodeView(APIView):
#     queryset = UserAccount.objects.all()
#     serialize_class = ValidEmailSerializer

#     # we should make use of serializer to validate 
#     def post(self, request, format=None):
#         serializer = self.serialize_class(data=request.data)

#         if not serializer.is_valid():
#              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
#         email = serializer.validated_data.get("email")
#         try:
#             account = self.queryset.get(email=email)

#         except UserAccount.DoesNotExist:
#             return Response({"message":"User account not found"}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             logger.error(f"Error retreiving account: {str(e)}")
#             return Response({"message":"Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#         code = generate_verification_code()
#         try:
#             account.code = code
#             account.save()
#         except Exception as e:
#             logger.error(f"Error updating account with otp secret: {str(e)}")
#             return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#         return Response({"code":code}, status=status.HTTP_200_OK)


        
# class EmailCheckingView(APIView):
#     queryset = UserAccount.objects.all()
#     serializer_class = ValidEmailSerializer
    
#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)

#         try:
#             serializer.is_valid(raise_exception=True)
#         except serializers.ValidationError as e:
#             logger.error(f"Validation error {str(e)}")
#             return Response({"errors":serializer.errors, "message":serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)
      
#         email = serializer.validated_data.get("email") 
     
#         try:
#             self.queryset.get(email=email)
#         except UserAccount.DoesNotExist:
#             return Response({"message":"User account not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         except Exception as e:
#             logger.error(f"Error retreiving account:  {str(e)}")
#             return Response({"message":"Errorr retreiving account"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#         return Response({"message":"account found"},status=status.HTTP_200_OK)
