from django.shortcuts import render
from core.abstract.viewsets import AbstractViewSet
from core.comment.models import Comment
from core.comment.serializer import CommentSerializer
from rest_framework.permissions import AllowAny
from core.auth.permissions.permissions import UserPermission
# Create your views here.

class CommentViewSet(AbstractViewSet):
    http_method_names=['get', 'post', 'put', 'delete']
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)
    
    
    def get_obj(self):
        obj=Comment.objects.get_object_by_id(self.kwargs['pk'])
        self.check_object_permissions(self.request,obj)
        
        return obj