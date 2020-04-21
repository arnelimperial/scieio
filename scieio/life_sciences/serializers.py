from rest_framework import serializers
from scieio.life_sciences import models


class LifeScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LifeScience
        fields = ('id', 'category', 'name', 'slug', 'created', 'updated')

