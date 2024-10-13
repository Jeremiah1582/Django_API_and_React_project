from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from .serializers import UserSerializer
from .models import User 
from core.abstract.viewsets import AbstractViewSet


class UserViewset(AbstractViewSet):
    http_method_names= ('get', 'patch')
    permission_classes= (IsAuthenticated,)
    serializer_class= UserSerializer
    
    def get_queryset(self):
         # http Request obj:
                # request object contains instance of User model, only if client is authorized! otherwise instance of anonymousUser
                # request object has an attribute user that represents the user who made the request  
        if self.request.user.is_superuser:
            return User.objects.prefetch_related()
        return User.objects.exclude(is_superuser=True)

    def get_object(self):
        obj= User.objects.get_object_by_id(self.kwargs['pk']) #extracting pk from a route      
        self.check_object_permissions(self.request, obj)
        return obj
    
    
    

    
        


