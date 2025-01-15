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
        return UserListSeriaiizer
    # serializer_class = UserRegistrationSerializer
    queryset = User.objects.all().order_by('-id')

    def get_permissions(self):
        if sel.action == 'create':
            self.permissions_class = AllowAny
        else:
            super().get_permissions_class = IsAuthenticated
        return super().get_permissions()