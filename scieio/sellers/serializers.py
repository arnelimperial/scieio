from rest_framework import serializers
from scieio.sellers import models


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Seller
        fields = (
            'id',
            'service_line',
            'client_manufacturer',
            'name',
            'slug',
            'location',
            'website',
            'description',
            'shipping_policy',
            'return_policy',
            'created',
            'updated'
        )
