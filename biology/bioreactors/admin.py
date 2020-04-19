from django.contrib import admin
from . import models


class BioReactorAdmin(admin.ModelAdmin):
    list_display = (
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


admin.site.register(models.BioReactor, BioReactorAdmin)
