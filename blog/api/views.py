from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import (
                   CreateModelMixin,
                   ListModelMixin,
                   RetrieveModelMixin,
                   DestroyModelMixin,)
from rest_framework.permissions import IsAuthenticated, AllowAny
from blog.api.serializers import (
                    UserRegistrationSerializer,
                    UserListSerializer,
                    UserInfoSerializer,
                    PostListSerializer,
                    PostInfoSerializer,
                    PostCreateUpdateSerializer,
                    CommentSerializer,
                   )
from blog.models import User, Post, Comment
from django.core.exceptions import PermissionDenied


class UserViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet,
):
    def get_serializer_class(self):
        if self.action == "create":
            return UserRegistrationSerializer
#         if self.action == "retrieve":
#             return UserRetrieveSerializer

        if self.action == "retrieve":
            return UserInfoSerializer
        return UserListSerializer
    queryset = User.objects.all().order_by('-id')

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by("-id")
    permission_class = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action == 'retrieve':
            return PostInfoSerializer
        return PostCreateUpdateSerializer

    def perform_update(self, serializer):
        instance = self.get_object()

        if instance.author != self.request.user:
            raise PermissionDenied('Вы не являетесь автором этого поста')
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Вы не являетесь автором этого поста')
        instance.delete()


class CommentViewSet(
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = Comment.objects.all().order_by('-id')
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['post__id']

    def perfomr_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Вы не являетесь автором этого комментария.')
        instance.delete()


