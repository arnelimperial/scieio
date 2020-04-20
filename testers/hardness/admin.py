from django.contrib import admin
from . import models


class HardnessAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'tester',
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


admin.site.register(models.Hardness, HardnessAdmin)
