from rest_framework import serializers
from . import models


class DispositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Disposition
        fields = (
            'id',
            'semiconductor',
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
