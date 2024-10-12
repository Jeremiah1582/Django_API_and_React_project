from core.user.models import User

 
def test_user():
    user_test_data={ 
                    'first_name':'test123',
                    'last_name':'testing123',
                    'email':'123@123brw.com',
                    'username':'tester123',
                    'password':'test_password123'
                    }
    return user_test_data