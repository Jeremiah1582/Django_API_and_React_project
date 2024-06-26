from rest_framework.serializers import SlugRelatedField
from rest_framework.exceptions import ValidationError
from core.abstract.serializers import AbstractSerializer
from core.comment.models import Comment
from core.user.models import User
from core.user.serializers import UserSerializer
from core.post.models import Post

class CommentSerializer(AbstractSerializer): 
    author = SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    post = SlugRelatedField(queryset=Post.objects.all(), slug_field='public_id')
    
    class Meta:
        model = Comment
        fields= '__all__'
    
       