from django.shortcuts import render
from rest_framework import viewsets
from scieio.immunoassay import models, serializers


class ImmunoAssayViewSet(viewsets.ModelViewSet):
    queryset = models.ImmunoAssay.objects.all()
    serializer_class = serializers.ImmunoAssaySerializer
