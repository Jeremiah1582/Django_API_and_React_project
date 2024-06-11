from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from core.abstract.models import AbstractManager, AbstractModel
# Create your models here.


class UserManager(BaseUserManager, AbstractManager):
    
    '''For creating Users and SuperUsers''' 
       
    # def get_object_by_public_id(self, public_id):
    #     # method is now redundant because it exists in AbstractManager
    #     try: 
    #         instance = self.get(public_id=public_id)
    #         return instance 
        
    #     except (ObjectDoesNotExist, ValueError, TypeError):
    #         return Http404  
        
    def create_user(self, username, email, password=None, **kwargs):
        '''create and return user '''
        # ERROR HANDLING if Values are non 
        if username is None: 
            raise TypeError('You must have a username')
        if email is None: 
            raise TypeError('user must have an email')
        if password is None: 
            raise TypeError('user must have a password')
        
        user = self.model(username = username, email= self.normalize_email(email) ,**kwargs )
        user.set_password(password)
        user.save(using = self._db)
        
        return user
    
    def create_superuser(self, username, email, password, **kwargs):
        '''create and return superuser with admin permissions'''
        
        if password is None: 
            raise TypeError('Superuser must have a password')
        if email is None: 
            raise TypeError('Superuser must have a email')
        if username is None: 
            raise TypeError('Superuser must have a Username')
        
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser=True
        user.save(using = self._db)
        
        return user


class User(AbstractBaseUser, PermissionsMixin, AbstractModel): 
    # public_id = models.UUIDField()                   # defined in AbstractModel
    username= models.CharField(db_index=True,  max_length=255, unique= True)
    first_name= models.CharField(max_length=70)
    last_name= models.CharField( max_length=70)
    
    email = models.EmailField(db_index=True, unique= True)
    is_active= models.BooleanField(default=True)
    is_superuser= models.BooleanField(default=False)
    
    
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True)

    # created= models.DateTimeField(auto_now= True)    # defined in AbstractModel
    # updated= models.DateTimeField(auto_now_add=True) # defined in AbstractModel
  
    USERNAME_FIELD='email'
    REQUIRED_FIELD=['username']
        
    objects=UserManager()
    
    
    def __str__(self): 
        return f'{self.email}'
    
    @property
    def name(self): 
        return f'{self.first_name} , {self.last_name}'
    
