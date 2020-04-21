from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class VRViewSet(viewsets.ModelViewSet):
    queryset = models.VR.objects.all()
    serializer_class = serializers.VRSerializer
