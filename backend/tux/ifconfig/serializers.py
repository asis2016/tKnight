__author__ = 'Ashish'
__description__ = 'ifconfig/serializers.py'


from rest_framework import serializers


class IfconfigSerializer(serializers.Serializer):
    data = serializers.JSONField()