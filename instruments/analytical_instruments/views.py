from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class InstrumentationViewSet(viewsets.ModelViewSet):
    queryset = models.Instrumentation.objects.all()
    serializer_class = serializers.InstrumentationSerializer


