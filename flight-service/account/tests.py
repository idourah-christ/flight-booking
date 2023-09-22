from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import UserAccount
from otp.generator import generate_verification_code

class OTPAuthenticationViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("account:otp-authentication")

        # Create a test user account with an OTP secret
        self.code = generate_verification_code()
        self.user = UserAccount.objects.create(email='test@example.com', code=self.code, password="kalilinux202",)

    def test_successful_authentication(self):
        data = {
            'email': 'test@example.com',
            'code': self.code 
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'authentification OTP reussie')

        account = UserAccount.objects.get(email=data.get("email"))

        self.assertIsNotNone(account)
        self.assertTrue(account.is_active)

    def test_missing_data(self):
        data = {
            'email': 'test@example.com'
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'missing code or email in data')

    def test_user_not_found(self):
        data = {
            'email': 'nonexistent@example.com',
            'code': self.code
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['message'], 'User account not found')

    def test_invalid_otp_code(self):
        data = {
            'email': 'test@example.com',
            'code': '654321'
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['message'], 'Invalid code {0}'.format(data.get('code')))

        account = UserAccount.objects.get(email=data.get("email"))

        self.assertIsNotNone(account)
        self.assertFalse(account.is_active)

class SendOTPCodeViewTest(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.url = reverse("account:generate-otp")

        self.user = UserAccount.objects.create(email="testexample@gmail.com", password="Renard38979")

    def test_otp_successfully_send(self):
        data = {
            "email":"testexample@gmail.com"
        }

        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_user_otp_secret_saved_successfully(self):
        data = {
            "email":"testexample@gmail.com"
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        code = response.data["code"]
        account = UserAccount.objects.get(email=data.get("email"))

        self.assertIsNotNone(account)
        self.assertTrue(account.code == code)
    
    def test_missing_data(self):
        data = {}

        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_not_found(self):
        data = {
            "email":"jonas@gmail.com"
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["message"], "User account not found")



class EmailCheckingViewTest(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.url = reverse("account:check-email-exist")
        self.account = UserAccount.objects.create(email="test@gmail.com", password="Jonas098733")
    """
    def test_missin_data(self):
        data = {}
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("errors",response.data)"""
    
    
    def test_email_already_used(self):
        data = {
            "email":"test@gmail.com"
        }
        res = self.client.post(self.url, data, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn(res.data["message"], "account found")
    
    
    def test_email_not_used(self):
        data = {
            "email":"alexandre@gmail.com"
        }
        res = self.client.post(self.url, data, format="json")
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(res.data["message"], "User account not found")

        


class UserAccountModelTest(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'phone': '123456789',
            'last_name': 'Doe',
            'first_name': 'John',
            'code': '123456',
            'password':"2348874840"
        }

    def test_create_user(self):
        # Create a user
        user = UserAccount.objects.create_user(**self.user_data)
        
        # Verify user properties
        self.assertEqual(user.email, self.user_data['email'])
        self.assertEqual(user.phone, self.user_data['phone'])
        self.assertEqual(user.last_name, self.user_data['last_name'])
        self.assertEqual(user.first_name, self.user_data['first_name'])
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.code, self.user_data['code'])

        # Verify user string representation
        self.assertEqual(str(user), self.user_data['email'])

    def test_create_superuser(self):
        # Create a superuser
        superuser = UserAccount.objects.create_superuser(**self.user_data)
        
        # Verify superuser properties
        self.assertEqual(superuser.email, self.user_data['email'])
        self.assertEqual(superuser.phone, self.user_data['phone'])
        self.assertEqual(superuser.last_name, self.user_data['last_name'])
        self.assertEqual(superuser.first_name, self.user_data['first_name'])
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertEqual(superuser.code, self.user_data['code'])

        # Verify superuser string representation
        self.assertEqual(str(superuser), self.user_data['email'])

