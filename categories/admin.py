from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created', 'updated')


admin.site.register(models.Category, CategoryAdmin)
