from rest_framework import serializers

from identification.models import ServiceCenter, Record, Fingerprints


class ServiceCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCenter
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class FingerPrintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fingerprints
        fields = '__all__'
