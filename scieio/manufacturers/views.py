from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer
