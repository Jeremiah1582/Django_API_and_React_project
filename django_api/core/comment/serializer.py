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
    
    def validate_author(self, value): 
        if self.context["request"].user != value:
            raise ValidationError('you cant create a post for another user')
        return value
    
    def validate_post(self, value): 
        if self.instance: 
            return self.instance.post
        return value
    
    def to_representation(self, instance):
        rep = super().to_representation(instance) # Returnse like object 
        author= User.objects.get_object_by_id(rep['author'])
        rep['author'] = UserSerializer(author).data
        
        return rep 
        
    class Meta:
        model = Comment
        fields= '__all__'
    
       