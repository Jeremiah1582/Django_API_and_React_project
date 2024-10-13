from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()

class AuthViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.login_url = reverse('auth-login-list')
        self.refresh_url = reverse('auth-refresh-list')
        self.register_url = reverse('auth-register-list')
        self.user_data = {
            'username': 'testuser987',
            'email': 'test987@example.com',
            'password': 'testpassword123'
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_login_success(self):
        response = self.client.post(self.login_url, {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_failure(self):
        response = self.client.post(self.login_url, {
            'email': self.user_data['email'],
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_refresh_token(self):
        # First, login to get a refresh token
        login_response = self.client.post(self.login_url, {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        })
        refresh_token = login_response.data['refresh']

        # Now use the refresh token to get a new access token
        response = self.client.post(self.refresh_url, {'refresh': refresh_token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_refresh_token_failure(self):
        response = self.client.post(self.refresh_url, {'refresh': 'invalid_token'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class RegisterViewSetTestCase(TestCase): 
    def setUp(self): 
        self.client = APIClient()
        self.register_url = reverse('auth-register-list')

        self.new_user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'newuser987',
            'email': 'newuser987@example.com',
            'password': 'newuserpassword123'
        }
        self.new_user = User.objects.create_user(**self.new_user_data)
        
    def test_register_success(self):
        response = self.client.post(self.register_url, self.new_user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email=self.new_user['email']).exists())

    def test_register_failure_existing_email(self):
        response = self.client.post(self.register_url, self.new_user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def register_fail_existing_username(self): 
        response = self.client(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
