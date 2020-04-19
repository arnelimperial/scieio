from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class ReagentViewSet(viewsets.ModelViewSet):
    queryset = models.Reagent.objects.all()
    serializer_class = serializers.ReagentSerializer
