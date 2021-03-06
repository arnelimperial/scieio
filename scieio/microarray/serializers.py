from rest_framework import serializers
from . import models


class MicroarrAyScannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MicroArrayScanner
        fields = (
            'id',
            'life_science',
            'name',
            'slug',
            'description',
            'product_code',
            'model',
            'condition',
            'warranty',
            'seller',
            'manufacturer',
            'image',
            'availability',
            'price',
            'created',
            'name',
            'slug',
            'created',
            'updated'
        )

