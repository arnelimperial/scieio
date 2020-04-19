from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class ConditionViewSet(viewsets.ModelViewSet):
    queryset = models.Condition.objects.all()
    serializer_class = serializers.ConditionSerializer
