from django.contrib import admin
from scieio.spectrometry import models


class SpectrometryAdmin(admin.ModelAdmin):
    list_display = ('id', 'instrumentation', 'name', 'slug', 'created', 'updated')


class GasMSAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'spectrometer',
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


class LiquidMSAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'spectrometer',
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


admin.site.register(models.Spectrometry, SpectrometryAdmin)
admin.site.register(models.GasMS, GasMSAdmin)
admin.site.register(models.LiquidMS, LiquidMSAdmin)
