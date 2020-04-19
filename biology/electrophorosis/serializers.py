from rest_framework import serializers
from . import models


class ElectrophorosisCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ElectrophorosisCategory
        fields = ('id', 'life_science', 'name', 'slug', 'created', 'updated')

#
# class GCChromaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.GCChroma
#         fields = ('id', 'chromatography_category', 'name', 'slug', 'created', 'updated')
#
#
# class LCChromaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.LCChroma
#         fields = ('id', 'chromatography_category', 'name', 'slug', 'created', 'updated')
#
#
# class GCSystemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.GCSystem
#         fields = (
#             'id',
#             'gc_category',
#             'name',
#             'slug',
#             'description',
#             'product_code',
#             'model',
#             'condition',
#             'warranty',
#             'seller',
#             'manufacturer',
#             'image',
#             'availability',
#             'price',
#             'created',
#             'name',
#             'slug',
#             'created',
#             'updated'
#         )
#
#
# class LCSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.LC
#         fields = (
#             'id',
#             'lc_category',
#             'name',
#             'slug',
#             'description',
#             'product_code',
#             'model',
#             'condition',
#             'warranty',
#             'seller',
#             'manufacturer',
#             'image',
#             'availability',
#             'price',
#             'created',
#             'name',
#             'slug',
#             'created',
#             'updated'
#         )
