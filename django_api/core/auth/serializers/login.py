from rest_framework_simplejwt.serializers import TokenObtainPairSerializer #generate a pair of access and refresh tokens
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login

from core.user.serializers import UserSerializer

class LoginSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs): #overriding. func call when is_valid is called 
        data = super().validate(attrs) #calling the parent class validate method
        
        refresh= self.get_token(self.user)
        data['user']= UserSerializer(self.user).data #added to the validated data
        data['refresh']= str(refresh)                #added to the validated data
        data['access']= str(refresh.access_token)    #added to the validated data
       
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
            
        return data