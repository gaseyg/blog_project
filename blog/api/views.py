from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
                   CreateModelMixin,
                   ListModelMixin,
                   RetrieveModelMixin,)
from rest_framework.permissions import IsAuthenticated, AllowAny
from blog.api.serializers import (
                   UserRegistrationSerializer,
                   UserListSerializer,
#                  UserRetrieveSerializer,
                   )
from blog.models import User


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
        return UserListSerializer
    queryset = User.objects.all().order_by('-id')

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()