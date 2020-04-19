from django.contrib import admin
from . import models


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'website', 'description', 'created', 'updated')


admin.site.register(models.Manufacturer, ManufacturerAdmin)
