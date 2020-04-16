from django.contrib import admin
from . import models


class SellerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
        'location',
        'website',
        'description',
        'shipping_policy',
        'return_policy',
        'created',
        'updated'
    )


admin.site.register(models.Seller, SellerAdmin)
