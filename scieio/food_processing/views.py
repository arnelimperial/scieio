from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class FoodProcessingViewSet(viewsets.ModelViewSet):
    queryset = models.FoodProcessing.objects.all()
    serializer_class = serializers.FoodProcessingSerializer
