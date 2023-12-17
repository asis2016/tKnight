# disk/serializers.py

from rest_framework import serializers


class DiskSerializer(serializers.Serializer):
    data = serializers.JSONField()
