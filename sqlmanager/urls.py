from rest_framework.routers import DefaultRouter
from .views import SystemViewSet

router = DefaultRouter()
router.register(r'systems', SystemViewSet, basename='system')

urlpatterns = router.urls
