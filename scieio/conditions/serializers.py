from rest_framework import serializers
from . import models


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Condition
        fields = ('id', 'name', 'slug', 'created', 'updated')
