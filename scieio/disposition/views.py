from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class DispositionViewSet(viewsets.ModelViewSet):
    queryset = models.Disposition.objects.all()
    serializer_class = serializers.DispositionSerializer
