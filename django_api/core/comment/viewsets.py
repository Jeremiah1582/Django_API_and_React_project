from django.shortcuts import render
from core.abstract.viewsets import AbstractViewSet
from core.comment.models import Comment
from core.comment.serializer import CommentSerializer
# Create your views here.

class CommentViewSet(AbstractViewSet):
    http_method_names=['get', 'post', 'put', 'delete']
    serializer_class = CommentSerializer
 
    # def get_queryset(self):
    #     comment = 
    #     return comment    