from rest_framework_nested import routers
from core.user.viewsets import UserViewset
from core.post.viewsets import PostViewSet
from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets.login import LoginViewSet 
from core.auth.viewsets.refresh import RefreshViewSet
from core.comment.viewsets import CommentViewSet

router= routers.SimpleRouter()


# USER
router.register(
    prefix= r'user', #name of endpoint 
    viewset=UserViewset, #viewset class
    basename='user' #helps django with registry purposes
    ) 

# AUTH 
router.register(
    prefix= r'auth/register', 
    viewset=RegisterViewSet, 
    basename= 'auth-register'
    )

router.register(
    prefix=r'auth/login',
    viewset=LoginViewSet,
    basename= 'auth-login'
    )

router.register(
    prefix=r'auth/refresh',
    viewset= RefreshViewSet,
    basename='auth-refresh'
)

# POSTS


router.register(
    prefix=r'post',
    viewset= PostViewSet,
    basename='post'
)
# -----Nested Routes-----
posts_router = routers.NestedSimpleRouter( # Making post a parent route
    parent_router=router, 
    parent_prefix=r'post', #declaring that the nested route will be under the "post" route 
    lookup='post' #regex 
    )
# regestering nested routes 
posts_router.register(
    prefix=r'comment',
    viewset= CommentViewSet,
    basename='post-comment'
)



# -----------------

urlpatterns = [
    *router.urls,
    *posts_router.urls
]

# BASE_DIR= Path(__file__).parent
# AUTH= BASE_DIR/'auth'
# VIEWSETS = BASE_DIR/AUTH/'viewsets'


# with open(VIEWSETS) as viewsets_dir:
#     print(viewsets_dir)

