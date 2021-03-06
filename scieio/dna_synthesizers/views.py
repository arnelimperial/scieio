from django.shortcuts import render
from rest_framework import viewsets
from scieio.dna_synthesizers import models, serializers


class DNASynthesizerViewSet(viewsets.ModelViewSet):
    queryset = models.DNASynthesizer.objects.all()
    serializer_class = serializers.DNASynthesizerSerializer
