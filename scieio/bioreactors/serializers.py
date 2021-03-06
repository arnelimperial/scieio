from rest_framework import serializers
from scieio.bioreactors import models


class BioReactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BioReactor
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

