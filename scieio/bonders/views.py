from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class BonderViewSet(viewsets.ModelViewSet):
    queryset = models.Bonder.objects.all()
    serializer_class = serializers.BonderSerializer
