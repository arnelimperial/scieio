from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class HardnessViewSet(viewsets.ModelViewSet):
    queryset = models.Hardness.objects.all()
    serializer_class = serializers.HardnessSerializer
