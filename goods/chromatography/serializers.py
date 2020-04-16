from rest_framework import serializers
from . import models


class ChromaCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChromaCategory
        fields = ('id', 'name', 'slug', 'created', 'updated')


class GCChromaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GCChroma
        fields = ('id', 'name', 'slug', 'created', 'updated')


class LCChromaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LCChroma
        fields = ('id', 'name', 'slug', 'created', 'updated')
