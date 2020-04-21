from django.contrib import admin
from . import models


class DispositionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'semiconductor',
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


admin.site.register(models.Disposition, DispositionAdmin)
