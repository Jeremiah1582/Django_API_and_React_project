from rest_framework import routers
from core.user.viewsets import UserViewset
from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets import LoginViewSet #shorter syntax due to viewset __init__.py file

router= routers.SimpleRouter()

router.register(
    prefix= r'user', #name of endpoint 
    viewset=UserViewset, #viewset class
    basename='user' #helps django with registry purposes
    ) 

router.register(
    prefix= r'auth/register', 
    viewset=RegisterViewSet, 
    basename= 'auth-register'
    )

router.register(
    prefix='auth/login',
    viewset=LoginViewSet,
    basename= 'auth-login'
    )

urlpatterns = [
    *router.urls,
]

