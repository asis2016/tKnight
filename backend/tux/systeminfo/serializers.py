# systeminfo/serializers.py

from rest_framework import serializers


class SysinfoSerializer(serializers.Serializer):
    data = serializers.JSONField()