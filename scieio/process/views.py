from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class ProcessViewSet(viewsets.ModelViewSet):
    queryset = models.Process.objects.all()
    serializer_class = serializers.ProcessSerializer
