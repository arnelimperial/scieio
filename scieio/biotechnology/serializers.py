from rest_framework import serializers
from scieio.biotechnology import models


class BioTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BioTech
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

