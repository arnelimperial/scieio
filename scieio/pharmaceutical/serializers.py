from rest_framework import serializers
from . import models


class PharmaceuticalEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PharmaceuticalEquipment
        fields = (
            'id',
            'process_category',
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

