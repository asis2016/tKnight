# sensors/serializers.py

from rest_framework import serializers


class SpeedtestapiSerializer(serializers.Serializer):
    data = serializers.JSONField()