from rest_framework import serializers


# pylint: disable=abstract-method
class UsageSerializer(serializers.Serializer):
    total = serializers.IntegerField()
    used = serializers.IntegerField()
    free = serializers.IntegerField()


# pylint: disable=abstract-method
class StatusSerializer(serializers.Serializer):
    storage_usage = UsageSerializer()


# pylint: disable=abstract-method
class VersionSerializer(serializers.Serializer):
    api_version = serializers.CharField(read_only=True)


# pylint: disable=abstract-method
class InfoSerializer(serializers.Serializer):
    station_name = serializers.CharField(read_only=True)
