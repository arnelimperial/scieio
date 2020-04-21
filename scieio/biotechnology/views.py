from django.shortcuts import render
from rest_framework import viewsets
from scieio.biotechnology import models, serializers


class BioTechViewSet(viewsets.ModelViewSet):
    queryset = models.BioTech.objects.all()
    serializer_class = serializers.BioTechSerializer
