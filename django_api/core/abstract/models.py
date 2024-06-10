from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
import uuid
from core.user.models import User

# Create your models here.
class AbstractManager(models.Manager):
    '''Return instance of object if public_id is found in DB, otherwise return 404'''
    
    def get_object_by_id(self, _id):
        try: 
            instance= self.get(public_id=_id)
            return instance
        except (ValueError, ObjectDoesNotExist, TypeError):
            return Http404
        

class AbstractModel(models.Model): 
    public_id =models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    created= models.DateTimeField(auto_now_add=True )
    updated= models.DateTimeField(auto_now=True )
    
    objects = AbstractManager()
    
    class Meta: 
        abstract= True

    

    