from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from core.fixtures.user import test_user
from core.user.models import User
# Create your tests here.f


class Test_Auth_ViewSet(TestCase):
    endpoint = '/api/auth/'
   

    def setup(self):
        self.client = APIClient()
        self.user = User.objects.create_user(**test_user)
        
        
    def test_login_success(self):
        login_details = {
            'email': self.user.email,
            'password': 'test_password123'
        }
       
        response = self.client.post(self.endpoint+'login/', login_details)
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR	

