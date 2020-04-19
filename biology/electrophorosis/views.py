from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class ElectrophorosisCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.ElectrophorosisCategory.objects.all()
    serializer_class = serializers.ElectrophorosisCategorySerializer

#
# class GCChromaViewSet(viewsets.ModelViewSet):
#     queryset = models.GCChroma.objects.all()
#     serializer_class = serializers.GCChromaSerializer
#
#
# class LCChromaViewSet(viewsets.ModelViewSet):
#     queryset = models.LCChroma.objects.all()
#     serializer_class = serializers.LCChromaSerializer
#
#
# class GCSystemViewSet(viewsets.ModelViewSet):
#     queryset = models.GCSystem.objects.all()
#     serializer_class = serializers.GCSystemSerializer
#
#
# class LCViewSet(viewsets.ModelViewSet):
#     queryset = models.LC.objects.all()
#     serializer_class = serializers.LCSerializer
