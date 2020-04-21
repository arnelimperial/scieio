from django.shortcuts import render
from rest_framework import viewsets
from scieio.spectrometry import models, serializers


class SpectrometryViewSet(viewsets.ModelViewSet):
    queryset = models.Spectrometry.objects.all()
    serializer_class = serializers.SpectrometrySerializer


class GasMSViewSet(viewsets.ModelViewSet):
    queryset = models.GasMS.objects.all()
    serializer_class = serializers.GasMSSerializer


class LiquidMSViewSet(viewsets.ModelViewSet):
    queryset = models.LiquidMS.objects.all()
    serializer_class = serializers.LiquidMSSerializer
