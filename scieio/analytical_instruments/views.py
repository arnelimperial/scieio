from django.shortcuts import render
from rest_framework import viewsets
from scieio.analytical_instruments import models, serializers


class InstrumentationViewSet(viewsets.ModelViewSet):
    queryset = models.Instrumentation.objects.all()
    serializer_class = serializers.InstrumentationSerializer


