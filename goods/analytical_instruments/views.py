from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class InstrumentCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.InstrumentCategory.objects.all()
    serializer_class = serializers.InstrumentCategorySerializer


