from django.shortcuts import render
from rest_framework import viewsets
from scieio.elemental_analyzers import models, serializers


class ElementalAnalyzerViewSet(viewsets.ModelViewSet):
    queryset = models.ElementalAnalyzer.objects.all()
    serializer_class = serializers.ElementalAnalyzerSerializer
