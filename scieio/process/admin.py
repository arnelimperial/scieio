from django.contrib import admin
from . import models


class ProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'slug', 'created', 'updated')


admin.site.register(models.Process, ProcessAdmin)
