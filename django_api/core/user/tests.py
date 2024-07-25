from django.test import TestCase
from core.user.models import User

# Create your tests here.
# utility function
user_data={'first_name':'test1', 'last_name':'testing1', 'email':'123@123.com', 'username':'tester1212', 'password':'test_password123'}
super_user_data={'first_name':'superuser', 'last_name':'testing_super', 'email':'superuser@123.com', 'username':'SuperTester1212', 'password':'1234567890'}

def create_user_utility_func(user_data):
    test_user= User.objects.create_user(**user_data)
    return test_user

def create_superuser_utility_func(user_data):
    test_super_user= User.objects.create_superuser(**user_data)
    return test_super_user
    

class Test_User_Model(TestCase): 
    '''unit tests related to the user module function'''
    
    def test_create_user_method(self): 
        '''testing create_user() method in core.user.modules'''
        self.assertIsInstance(create_user_utility_func(user_data), User)
        
    
    def test_create_super_user_method(self): 
        '''testing to see if a super user is created'''
        super_user = create_superuser_utility_func(super_user_data)
        self.assertIsInstance(super_user, User)
        self.assertEqual(super_user.is_superuser,True)
        
        
#---------------functional programming --------------
# import pytest
# from core.user.models import User

# data_user ={
#     "username": "test_user",
#     "email": "test@gmail.com",
#     "first_name": "Test",
#     "last_name": "User",
#     "password": "test_password"
# }

# super_userdata={
#     "username": "test_super_user",
#     "email": "testsuperuser@gmail.com",
#     "first_name": "Test2",
#     "last_name": "SuperUser",
#     "password": "test_super_user_password"
# }
        
        
# @pytest.mark.django_db
# def test_create_user():
#     user = User.objects.create_user(**data_user)
#     assert user.username== data_user['username']
#     assert user.email== data_user['email']
#     assert user.first_name== data_user['first_name']
#     assert user.last_name== data_user['last_name']

# @pytest.mark.django_db
# def test_create_super_user():
#     user = User.objects.create_superuser(**data_user)
#     assert user.username== data_user['username']
#     assert user.email== data_user['email']
#     assert user.first_name== data_user['first_name']
#     assert user.last_name== data_user['last_name']
#     assert user.is_superuser == True
#     # assert user.is_staff == True
    
   
    
    
    