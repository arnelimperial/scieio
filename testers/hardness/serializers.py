from rest_framework import serializers
from . import models


class HardnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hardness
        fields = (
            'id',
            'tester',
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
