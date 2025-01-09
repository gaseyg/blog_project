from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from blog.api.serializers import UserRegistrationSerializer, UserListSerializer


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
