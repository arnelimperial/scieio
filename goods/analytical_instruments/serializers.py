from rest_framework import serializers
from . import models


class InstrumentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InstrumentCategory
        fields = ('id', 'name', 'slug', 'created', 'updated')



