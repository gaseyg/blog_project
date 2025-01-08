from rest_framework.routers import SimpleRouter

from blog.api.views import UserViewSet

router = SimpleRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = router.urls