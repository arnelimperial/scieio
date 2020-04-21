from django.shortcuts import render
from rest_framework import viewsets
from scieio.sellers import models
from scieio.sellers import serializers


class SellerViewSet(viewsets.ModelViewSet):
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerSerializer
