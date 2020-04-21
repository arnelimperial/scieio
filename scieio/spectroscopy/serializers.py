from rest_framework import serializers
from . import models


class SpectroscopySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Spectroscopy
        fields = ('id', 'instrumentation', 'name', 'slug', 'created', 'updated')


class AtomicAbsorptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AtomicAbsorption
        fields = (
            'id',
            'spectroscopy_category',
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


class SpectrophotometerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Spectrophotometer
        fields =  fields = (
            'id',
            'spectroscopy_category',
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


class ICPSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ICP
        fields = (
            'id',
            'spectroscopy_category',
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


class FTIRSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FTIR
        fields = (
            'id',
            'spectroscopy_category',
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
