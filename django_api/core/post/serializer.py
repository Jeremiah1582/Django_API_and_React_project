from core.abstract.serializers import AbstractSerializer
from rest_framework import serializers
from core.user.models import User
from core.post.models import Post
from rest_framework.exceptions import ValidationError

class PostSerializer(AbstractSerializer): 
    '''inherits id, created and updated '''
    author = serializers.SlugRelatedField(queryset =User.objects.all(), slug_field='public_id')

    def validate_author(self,value):
        if self.context['request'].user !=value:
            raise ValidationError('you can not create a post for another user')
        return value
    
    class Meta: 
        model = Post
        fields=['id', 'author', 'body', 'edited', 'created', 'updated']
        read_only_fields= ['edited']