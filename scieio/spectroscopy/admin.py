from django.contrib import admin
from . import models


class SpectroscopyAdmin(admin.ModelAdmin):
    list_display = ('id', 'instrumentation', 'name', 'slug', 'created', 'updated')


class AtomicAbsorptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'spectroscopy_category',
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


class SpectrophotometerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'spectroscopy_category',
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


class ICPAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'spectroscopy_category',
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


class FTIRAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'spectroscopy_category',
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


admin.site.register(models.Spectroscopy, SpectroscopyAdmin)
admin.site.register(models.AtomicAbsorption, AtomicAbsorptionAdmin)
admin.site.register(models.Spectrophotometer, SpectrophotometerAdmin)
admin.site.register(models.ICP, ICPAdmin)
admin.site.register(models.FTIR, FTIRAdmin)
