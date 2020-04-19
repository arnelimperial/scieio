from rest_framework import serializers
from . import models


class SpectrometrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Spectrometry
        fields = ('id', 'instrumentation', 'name', 'slug', 'created', 'updated')


class GasMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GasMS
        fields = (
            'id',
            'spectrometer',
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


class LiquidMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LiquidMS
        fields = (
            'id',
            'spectrometer',
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
