from rest_framework import serializers
from scieio.analytical_instruments import models


class InstrumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instrumentation
        fields = ('id', 'category', 'name', 'slug', 'created', 'updated')



