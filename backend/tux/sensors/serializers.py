# sensors/serializers.py

from rest_framework import serializers


class SensorsSerializer(serializers.Serializer):
    data = serializers.JSONField()