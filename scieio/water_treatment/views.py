from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class WaterTreatmentViewSet(viewsets.ModelViewSet):
    queryset = models.WaterTreatment.objects.all()
    serializer_class = serializers.WaterTreatmentSerializer
