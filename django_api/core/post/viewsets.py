from core.abstract.viewsets import AbstractViewSet
# Create your views here.
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.post.models import Post 
from core.post.serializer import PostSerializer
from rest_framework.response import Response
from rest_framework import status

class PostViewSet(AbstractViewSet): 
    http_method_names=['post','get', 'put', 'delete']
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
    
    
    def get_queryset(self): 
        '''get all posts '''
      
        posts = Post.objects.all()
        return posts
    
    def get_object(self):
        
        obj = Post.objects.get_object_by_id(self.kwargs['pk'])
        self.check_object_permissions(self.request,obj)
        return obj
    
    def create(self, request, *args, **kwargs): 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status= status.HTTP_201_CREATED)
    
    
        