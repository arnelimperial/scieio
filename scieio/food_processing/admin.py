from django.contrib import admin
from . import models


class FoodProcessingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'process_category',
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


admin.site.register(models.FoodProcessing, FoodProcessingAdmin)
