from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class BioReactorViewSet(viewsets.ModelViewSet):
    queryset = models.BioReactor.objects.all()
    serializer_class = serializers.BioReactorSerializer
