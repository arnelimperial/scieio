from django.contrib import admin
from . import models


class ConditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created', 'updated')


admin.site.register(models.Condition, ConditionAdmin)
