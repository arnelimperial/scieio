from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class DNASequencerViewSet(viewsets.ModelViewSet):
    queryset = models.DNASequencer.objects.all()
    serializer_class = serializers.DNASequencerSerializer
