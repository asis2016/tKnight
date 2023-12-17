__author__ = 'Ashish'
__description__ = 'process/serializers.py'


from rest_framework import serializers


class ProcessSerializer(serializers.Serializer):
    data = serializers.JSONField()