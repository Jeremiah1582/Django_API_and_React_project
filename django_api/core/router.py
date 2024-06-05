from rest_framework import routers
from core.user.viewsets import UserViewset
from core.auth.viewsets.register import RegisterViewSet

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

urlpatterns = [
    *router.urls,
]

