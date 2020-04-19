from rest_framework import serializers
from . import models


class InstrumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instrumentation
        fields = ('id', 'category', 'name', 'slug', 'created', 'updated')



