from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class TestSemiconductorViewSet(viewsets.ModelViewSet):
    queryset = models.TestSemiConductor.objects.all()
    serializer_class = serializers.TestSemiconductorSerializer
