from core.abstract.viewsets import AbstractViewSet
# Create your views here.
from core.post.models import Post 
from core.post.serializer import PostSerializer

class PostViewSet(AbstractViewSet): 
    serializer_class = PostSerializer
    
    def get_queryset(request): 
        posts = Post.objects.prefetch_related().order_by('created')
        return posts
    