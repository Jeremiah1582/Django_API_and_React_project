"""Serializers handle validation, transformation of data,  """

from rest_framework.serializers import SlugRelatedField
from rest_framework.exceptions import ValidationError
from core.abstract.serializers import AbstractSerializer
from core.comment.models import Comment
from core.user.models import User
from core.user.serializers import UserSerializer
from core.post.models import Post

class CommentSerializer(AbstractSerializer): 
    
    author = SlugRelatedField(queryset=User.objects.all(), slug_field='public_id') #searches queryset using instances public_id, returns public_id match
    post = SlugRelatedField(queryset=Post.objects.all(), slug_field='public_id') #contains public_id 
    
    def validate_author(self, value): 
        if self.context["request"].user!= value:
            raise ValidationError('you cant create a comment for another user')
        return value
    
    def validate_post(self, value): 
        if self.instance: 
            return self.instance.post
        return value
    
    def to_representation(self, instance):
        rep = super().to_representation(instance) # Returns - like object 
        author= User.objects.get_object_by_id(rep['author']) #
        rep['author'] = UserSerializer(author).data
        
        return rep 
    
    def update(self, instance, validated_data): 
        '''Every model serializer provides an instance attribute that holds the object that will be modified if there is a delete, put, or patch request. If this is a GET or POST request, this attribute is set to None.'''
        if not instance.edited: #set edited to true if not already
            validated_data['edited'] = True
        instance = super().update(instance, validated_data)
        return instance
    
    def delete(self, instance): 
        super()
    class Meta:
        model = Comment
        fields= '__all__' #all the fields that can be included in req or res 
        read_only_fields=["edited"]
        
        


       