from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User 
from core.abstract.viewsets import AbstractViewSet


class UserViewset(AbstractViewSet):
    http_method_names= ('get', 'patch')
    permission_classes= (AllowAny,)
    serializer_class= UserSerializer
 
    
    def get_queryset(self):
         # http Request obj:
                # request object contains instance of User model, only if client is authorized! otherwise instance of anonymousUser
                # request object has an attribute user that represents the user who made the request
        print(',................', self.request.user)
        if self.request.user.is_superuser:
            queryset= User.objects.prefetch_related()
        else:
            queryset= User.objects.exclude(is_superuser=True)
            
        serialized= self.get_serializer(queryset,many=True)
        return serialized.data
  

    def get_object(self):
        obj= User.objects.get_object_by_public_id(self.kwargs['pk']) #extracting pk from a route      
        self.check_object_permissions(self.request, obj)
        return obj
    
    
    

    
        


