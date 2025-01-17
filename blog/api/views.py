from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from blog.api.serializers import UserRegistrationSerializer, UserListSerializer
from blog.models import User


class UserViewSet(
    CreateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    def get_serializer_class(self):
        if self.action == "create":
            return UserRegistrationSerializer
        return UserListSerializer
    # serializer_class = UserRegistrationSerializer
    queryset = User.objects.all().order_by('-id')

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()