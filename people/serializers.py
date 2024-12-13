from requests import Response
from rest_framework import serializers

from .models import Patient, Record, ProfilePicture, Fingerprints, Tag, ServiceCenter

from rest_framework.utils.serializer_helpers import ReturnDict


class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = '__all__'


class ServiceCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCenter
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    profilePictures = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # tags = serializers.StringRelatedField(many=True)

    # tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Patient
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        satient = Patient.objects.create(**validated_data)
        if self.request.FILES:
            files = self.request.FILES
            for image in files.values():
                ProfilePicture.objects.create(satient=satient, picture=image)
        else:
            print('no files uploaded')
        return satient


class TagSerializer(serializers.ModelSerializer):
    # satients = PatientSerializer(read_only=True, many=True)
    satients = serializers.SerializerMethodField()
    service_centers = serializers.SerializerMethodField()

    def get_satients(self, obj):
        result = []

        for satient in obj.satient_set.all():
            serializer_class = PatientSerializer(satient)
            serialized_data = serializer_class.data
            print(type(serialized_data))
            serialized_data.pop('tags')
            result.append(serialized_data)
        return result

    def get_service_centers(self, obj):
        result = []

        for center in obj.servicecenter_set.all():
            serializer_class = ServiceCenterSerializer(center)
            serialized_data = serializer_class.data
            print(type(serialized_data))
            serialized_data.pop('tags')
            result.append(serialized_data)
        return result

    class Meta:
        model = Tag
        fields = '__all__'
        # fields = ['satients', 'serviceCenters']
        depth = 10


class TagNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class FingerPrintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fingerprints
        fields = '__all__'
