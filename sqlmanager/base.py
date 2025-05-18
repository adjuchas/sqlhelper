from rest_framework import viewsets, status
from rest_framework.response import Response
from django.utils import timezone
from .models import ChangeLog  # 假设模型已反向生成
from .serializers import ChangeLogSerializer  # 你需要自建该 serializer

class BaseModelViewSet(viewsets.ModelViewSet):
    change_log_target_type = None  # 子类必须设置

    def perform_create(self, serializer):
        instance = serializer.save()
        self._create_change_log(instance, 'create')
        return instance

    def perform_update(self, serializer):
        instance = serializer.save()
        self._create_change_log(instance, 'update')
        return instance

    def perform_destroy(self, instance):
        self._create_change_log(instance, 'delete')
        instance.delete()

    def _create_change_log(self, instance, action):
        ChangeLog.objects.create(
            target_type=self.change_log_target_type,
            target_id=instance.id,
            action=action,
            performed_by=self.request.user.username if self.request.user.is_authenticated else 'anonymous',
            performed_at=timezone.now(),
            description=f"{action.upper()} {self.change_log_target_type.upper()} [{instance}]"
        )
