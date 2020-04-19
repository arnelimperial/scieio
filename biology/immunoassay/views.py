from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class ImmunoAssayViewSet(viewsets.ModelViewSet):
    queryset = models.ImmunoAssay.objects.all()
    serializer_class = serializers.ImmunoAssaySerializer
