from rest_framework import serializers
from . import models


class TestSemiconductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestSemiConductor
        fields = ('id', 'category', 'name', 'slug', 'created', 'updated')

