from django.db import models
from core.abstract.models import AbstractModel, AbstractManager
from django.conf import settings
# Create your models here.

class PostManager(AbstractManager): 
    '''Abstract methods include: get_object_by_id(self,_id)'''
    pass
    

class Post(AbstractModel): 
    '''includes: public_id, created, updated'''
    author= models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete =models.CASCADE)
    # title=models.CharField(max_length=255)
    body= models.TextField()
    edited=models.BooleanField(default=False)
    
        
    objects= PostManager()
    
    def __str__(self): 
        return f'{self.author}-{self.created}-{self.title}-' 
    
    class Meta:
        db_table = 'core.post'
      
    
    

