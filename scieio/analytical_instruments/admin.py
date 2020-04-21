from django.contrib import admin
from scieio.analytical_instruments import models


class InstrumentationAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'slug', 'created', 'updated')


admin.site.register(models.Instrumentation, InstrumentationAdmin)
