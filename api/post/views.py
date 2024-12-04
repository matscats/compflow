from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers import PostSerializer
from .permissions import CanPublishPost
from .models import Post


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, CanPublishPost]
    queryset = Post.objects.all()
