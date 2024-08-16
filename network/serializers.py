from rest_framework import serializers
from .models import NetworkNode


class NetworkNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = ['id', 'name', 'contact_info', 'level', 'supplier', 'debt', 'created_at']

    def update(self, instance, validated_data):
        """Заппещает обновление поля 'Задолженность'"""
        validated_data.pop('debt', None)
        return super().update(instance, validated_data)
