from rest_framework import serializers
from scieio.dna_sequencer import models


class DNASequencerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DNASequencer
        fields = (
            'id',
            'life_science',
            'name',
            'slug',
            'description',
            'product_code',
            'model',
            'condition',
            'warranty',
            'seller',
            'manufacturer',
            'image',
            'availability',
            'price',
            'created',
            'name',
            'slug',
            'created',
            'updated'
        )

