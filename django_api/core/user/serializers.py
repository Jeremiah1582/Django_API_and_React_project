from rest_framework import serializers
from core.user.models import User

class UserSerializer(serializers.ModelSerializer):
    '''this class is used to serialize and deserialize data to and from a python dictionary so the data can be processed by the python backend or stored in the Database '''
    id = serializers.UUIDField(source='public_id', read_only= True, format='hex')
    created= serializers.DateTimeField(read_only= True)
    updated= serializers.DateTimeField(read_only= True)
    
    class Meta:
        model = User
        # List of all the fields that can be included in a request or a response
        fields=['id', 'username', 'first_name', 'last_name', 'bio', 'avatar', 'email', 'is_active',
                  'created', 'updated', 'is_superuser']
        #list of all the fields that only the user can read
        read_only_fields = ['is_active','is_superuser'] 
        
    # NOTE: read only fields will not be translated into Python Objects during deserialization
    