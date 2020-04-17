from rest_framework import serializers
from . import models


class ChromaCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChromaCategory
        fields = ('id', 'instrumentation', 'name', 'slug', 'created', 'updated')


class GCChromaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GCChroma
        fields = ('id', 'chromatography_category', 'name', 'slug', 'created', 'updated')


class LCChromaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LCChroma
        fields = ('id', 'chromatography_category', 'name', 'slug', 'created', 'updated')

#
# class GCSystemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.GCSystem
#         fields = (
#             'id',
#             'product_category',
#             'instrument_category',
#             'chromatography_category',
#             'gc_category',
#             'name',
#             'slug',
#             'description',
#             'product_id',
#             'model',
#             'condition',
#             'warranty',
#             'seller',
#             'manufacturer',
#             'image',
#             'price',
#             'created',
#             'name',
#             'slug',
#             'created',
#             'updated'
#         )
