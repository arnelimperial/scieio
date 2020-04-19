from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class ElementalAnalyzerViewSet(viewsets.ModelViewSet):
    queryset = models.ElementalAnalyzer.objects.all()
    serializer_class = serializers.ElementalAnalyzerSerializer
