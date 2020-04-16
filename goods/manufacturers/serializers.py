from rest_framework import serializers
from . import models


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ('id', 'name', 'slug', 'website', 'description', 'created', 'updated')
