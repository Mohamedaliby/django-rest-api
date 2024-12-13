from rest_framework import viewsets

from identification.models import Record, ServiceCenter, Fingerprints
from identification.serializers import RecordSerializer, ServiceCenterSerializer, FingerPrintSerializer


class RecordView(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class ServiceCenterView(viewsets.ModelViewSet):
    queryset = ServiceCenter.objects.all()
    serializer_class = ServiceCenterSerializer


class ServiceCenterView(viewsets.ModelViewSet):
    queryset = Fingerprints.objects.all()
    serializer_class = FingerPrintSerializer
