from django.contrib import admin
from . import models


class InstrumentCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created', 'updated')


admin.site.register(models.InstrumentCategory, InstrumentCategoryAdmin)
