from django.contrib import admin
from . import models


class ChromaCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created', 'updated')


admin.site.register(models.ChromaCategory, ChromaCategoryAdmin)
