from rest_framework import routers
from core.user.viewsets import UserViewset
from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets import LoginViewSet, RefreshViewSet #shorter syntax due to viewset __init__.py file


from pathlib import Path

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

router.register(
    prefix='auth/refresh',
    viewset= RefreshViewSet,
    basename='auth-refresh'
)

urlpatterns = [
    *router.urls,
]

# BASE_DIR= Path(__file__).parent
# AUTH= BASE_DIR/'auth'
# VIEWSETS = BASE_DIR/AUTH/'viewsets'


# with open(VIEWSETS) as viewsets_dir:
#     print(viewsets_dir)

