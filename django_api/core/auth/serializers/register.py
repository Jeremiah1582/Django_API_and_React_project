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
    
    def validate_first_name(self, value): 
        error=[]
        if len(value) < 3: 
            error.append("!! First name must be at least 3 characters long")
        if len(error)>0: 
            raise serializers.ValidationError(error)
        return value
    
    def validate_last_name(self, value): 
        error=[]
        if len(value) < 3: 
            error.append("!! Last name must be at least 3 characters long")
        if len(error)>0: 
            raise serializers.ValidationError(error)
        return value
    
     #any func with validate_. is automatically called when is_valid() is called in DRF
    def validate_password(self, value):
        error=[]
        if not re.search(r'[A-Z]',value):
            error.append("!! Password must have at least 1 capital letter")
        
        if not re.search(r'[0-9]',value):
            error.append("!! Password must have at least 1 Number")
        
        if len(error)>0: 
            raise serializers.ValidationError(error)
        
        return value
    
    def validate_email(self, value):
        error=[]
        if User.objects.filter(email=value).exists(): 
            error.append("!! Email already exists, you are already Registered")

        if len(error)>0: 
            raise serializers.ValidationError(error)
        return value
    
    def validate_username(self, value):
        error=[]
        if User.objects.filter(username=value).exists(): 
            error.append("!! username already exists")
    
        if len(error)>0: 
            raise serializers.ValidationError(error)
        return value
    
    
    
    class Meta: 
        model = User
        fields= ['id', 'bio', 'avatar', 'email', 'username', 'first_name',  'password']