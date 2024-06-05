from rest_framework import serializers
from core.user.models import User
from core.user.serializers import UserSerializer
import re 

class RegistrationSerializer(UserSerializer): 
    '''RegistrationSerializer for requests and user creation'''
# Making sure the password is at least 8 characters long, and no longer than 128 and can't be read by the user
    password = serializers.CharField(max_length= 128, min_length= 8, write_only=True, required= True) 

    def create(self, validated_data): 
        # Use the `create_user` method we wrote earlier for the UserManager to create a new user.
        return User.objects.create_user(**validated_data)
    
    
     #any func with validate_. is automatically called when is_valid() is called in DRF
    def validate_password(self, value):
        if len(value) < 8:
            # this len() check is redundant! validattion happening in password variable above
            raise serializers.ValidationError("password must be 8 character or more")
        
        if not re.search(r'[A-Z]',value):
            raise serializers.ValidationError("Password must have at least 1 capital letter")
        
        if not re.search(r'[0-9]',value):
            raise serializers.ValidationError("Password must have at least 1 Number")
        
        return value
    

  
            
    class Meta: 
        model = User
        fields= ['id', 'bio', 'avatar', 'email', 'username', 'first_name',  'password']