""" viewsets are for manipulating the data and returning the result"""

from django.shortcuts import render
from core.abstract.viewsets import AbstractViewSet
from core.comment.models import Comment
from core.comment.serializer import CommentSerializer
from rest_framework.permissions import AllowAny
from core.auth.permissions.permissions import UserPermission
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CommentViewSet(AbstractViewSet):
    http_method_names=('get', 'post', 'put', 'delete')
    serializer_class = CommentSerializer
    permission_classes = (UserPermission,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED )
        
     
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Comment.objects.all()#
        
        post_pk = self.kwargs['post_id']
        if post_pk is None:
            return Http404    
        queryset= Comment.objects.filter(
            post__public_id = post_pk 
            #post_ relates to the post object in the Comment model, related via foreignkey
          
            ) #lookup method, in "post" objects look up "public_id" that matches post_pk
        # post
        return queryset
      
        
    def get_object(self):
        obj=Comment.objects.get_object_by_id(self.kwargs['pk'])
        self.check_object_permissions(self.request,obj)
        return obj
    
   
    
    