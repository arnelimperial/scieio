from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class SellerViewSet(viewsets.ModelViewSet):
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerSerializer
