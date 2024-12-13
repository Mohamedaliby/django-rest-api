from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .models import Patient, Record, ProfilePicture, Tag, ServiceCenter
from .serializers import PatientSerializer, RecordSerializer, ProfilePictureSerializer, TagSerializer, \
    ServiceCenterSerializer, TagNameSerializer


class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    parser_classes = [MultiPartParser]

    def create(self, request, **kwargs):
        serializer = PatientSerializer(data=request.data)
        serializer.request = request
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListCreatePatient(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class RecordView(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class ProfilePictureView(viewsets.ModelViewSet):
    queryset = ProfilePicture.objects.all()
    serializer_class = ProfilePictureSerializer


class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagNameView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagNameSerializer


class ServiceCenterView(viewsets.ModelViewSet):
    queryset = ServiceCenter.objects.all()
    serializer_class = ServiceCenterSerializer
