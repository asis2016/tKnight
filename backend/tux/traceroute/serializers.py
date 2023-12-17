# sensors/serializers.py

from rest_framework import serializers


class TracerouteSerializer(serializers.Serializer):
    data = serializers.JSONField()