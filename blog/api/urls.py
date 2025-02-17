from rest_framework.routers import SimpleRouter

from blog.api.views import UserViewSet, PostViewSet, CommentsViewSet

router = SimpleRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentsViewSet, basename='comments')

urlpatterns = router.urls