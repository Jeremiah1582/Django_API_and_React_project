from django.db import models
from core.abstract.models import AbstractModel, AbstractManager
from core.post.models import Post
from core.user.models import User
from django.conf import settings

# Create your models here.
class CommentManager(AbstractManager):
    pass

class Comment(AbstractModel):
    author= models.ForeignKey(to = settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    post = models.ForeignKey(to='core_post.post',  on_delete=models.PROTECT)
    edited = models.BooleanField(default= False)
    body = models.TextField()
        
    objects= CommentManager()
    
    def __str__(self) -> str:
        return f'{self.author.name}'
   
    class Meta:
        db_table = 'core_comment'
       
      
    

    
    