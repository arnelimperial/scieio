from django.contrib import admin
from . import models


class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'location', 'website', 'phone', 'created', 'updated')


admin.site.register(models.Seller, SellerAdmin)
