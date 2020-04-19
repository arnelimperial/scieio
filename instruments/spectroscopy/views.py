from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class SpectroscopyViewSet(viewsets.ModelViewSet):
    queryset = models.Spectroscopy.objects.all()
    serializer_class = serializers.SpectroscopySerializer


class AtomicAbsorptionViewSet(viewsets.ModelViewSet):
    queryset = models.AtomicAbsorption.objects.all()
    serializer_class = serializers.AtomicAbsorptionSerializer


class SpectrophotometerViewSet(viewsets.ModelViewSet):
    queryset = models.Spectrophotometer.objects.all()
    serializer_class = serializers.SpectrophotometerSerializer


class ICPViewSet(viewsets.ModelViewSet):
    queryset = models.ICP.objects.all()
    serializer_class = serializers.ICPSerializer


class FTIRViewSet(viewsets.ModelViewSet):
    queryset = models.FTIR.objects.all()
    serializer_class = serializers.FTIRSerializer
