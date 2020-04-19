from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class MicroArrayScannerViewSet(viewsets.ModelViewSet):
    queryset = models.MicroArrayScanner.objects.all()
    serializer_class = serializers.MicroarrAyScannerSerializer
