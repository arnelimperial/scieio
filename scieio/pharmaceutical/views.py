from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class PharmaceuticalEquipmentViewSet(viewsets.ModelViewSet):
    queryset = models.PharmaceuticalEquipment.objects.all()
    serializer_class = serializers.PharmaceuticalEquipmentSerializer
