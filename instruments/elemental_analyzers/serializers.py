from rest_framework import serializers
from . import models


class ElementalAnalyzerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ElementalAnalyzer
        fields = (
            'id',
            'instrumentation',
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
