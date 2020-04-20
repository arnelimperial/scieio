from rest_framework import serializers
from . import models


class BonderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bonder
        fields = ('id', 'semiconductor', 'name', 'slug', 'created', 'updated')

