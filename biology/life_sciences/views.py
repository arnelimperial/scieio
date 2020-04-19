from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class LifeScienceViewSet(viewsets.ModelViewSet):
    queryset = models.LifeScience.objects.all()
    serializer_class = serializers.LifeScienceSerializer
