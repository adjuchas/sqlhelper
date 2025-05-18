from .models import SystemManagement
from .serializers import SystemManagementSerializer
from .base import BaseModelViewSet

class SystemViewSet(BaseModelViewSet):
    queryset = SystemManagement.objects.all()
    serializer_class = SystemManagementSerializer
    change_log_target_type = 'system'
