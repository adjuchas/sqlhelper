from rest_framework import serializers
from .models import ChangeLog, SystemManagement

class ChangeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeLog
        fields = '__all__'


class SystemManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemManagement
        fields = '__all__'