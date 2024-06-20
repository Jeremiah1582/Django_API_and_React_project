from core.abstract.serializers import AbstractSerializer
from rest_framework import serializers
from core.user.models import User
from core.post.models import Post
from rest_framework.exceptions import ValidationError
from core.user.serializers import UserSerializer

class PostSerializer(AbstractSerializer): 
    '''inherits id, created and updated '''
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    liked=serializers.SerializerMethodField()
    likes_count=serializers.SerializerMethodField()
    
    
    def validate_author(self,value):
        if self.context['request'].user !=value:
            raise ValidationError('you can not create a post for another user')
        return value
    
    def to_representation(self,instance): 
        rep = super().to_representation(instance) # converts instance to python native Dict
        author = User.objects.get_object_by_id(rep['author'])
        rep['author']= UserSerializer(author).data
        
        return rep
    
    def update(self, instance, validated_data):
        if not instance.edited: 
            validated_data['edited']=True
            
        instance = super().update(instance, validated_data)
        return instance
    
    def get_likes_count(self, instance): 
        return instance.liked_by.count()
    
    def get_liked(self, instance): 
        request = self.context.get('request', None)
        if request is None or request.user.is_anonymous: 
            return False
        return request.user.has_liked(instance)
    
        
    class Meta: 
        model = Post
        fields=['id', 'author', 'body', 'edited', 'created', 'updated', 'liked', 'likes_count']
        read_only_fields= ['edited'] 