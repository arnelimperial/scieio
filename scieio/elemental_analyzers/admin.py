from django.contrib import admin
from scieio.elemental_analyzers import models


class ElementalAnalyzerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'instrumentation',
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


admin.site.register(models.ElementalAnalyzer, ElementalAnalyzerAdmin)
