from django.contrib import admin
from . import models


class ElectrophorosisCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'life_science', 'name', 'slug', 'created', 'updated')

#
# class GCChromaAdmin(admin.ModelAdmin):
#     list_display = ('id', 'chromatography_category', 'name', 'slug', 'created', 'updated')
#
#
# class LCChromaAdmin(admin.ModelAdmin):
#     list_display = ('id', 'chromatography_category', 'name', 'slug', 'created', 'updated')
#
#
# class GCSystemAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'gc_category',
#         'name',
#         'slug',
#         'description',
#         'product_code',
#         'model',
#         'condition',
#         'warranty',
#         'seller',
#         'manufacturer',
#         'image',
#         'availability',
#         'price',
#         'created',
#         'name',
#         'slug',
#         'created',
#         'updated'
#     )
#
#
# class LCAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'lc_category',
#         'name',
#         'slug',
#         'description',
#         'product_code',
#         'model',
#         'condition',
#         'warranty',
#         'seller',
#         'manufacturer',
#         'image',
#         'availability',
#         'price',
#         'created',
#         'name',
#         'slug',
#         'created',
#         'updated'
#     )


admin.site.register(models.ElectrophorosisCategory, ElectrophorosisCategoryAdmin)
# admin.site.register(models.GCChroma, GCChromaAdmin)
# admin.site.register(models.LCChroma, LCChromaAdmin)
# admin.site.register(models.GCSystem, GCSystemAdmin)
# admin.site.register(models.LC, LCAdmin)
