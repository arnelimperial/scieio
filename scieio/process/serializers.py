from rest_framework import serializers
from . import models


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Process
        fields = ('id', 'category', 'name', 'slug', 'created', 'updated')

