from django.contrib import admin
from scieio.life_sciences import models


class LifeScienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'slug', 'created', 'updated')


admin.site.register(models.LifeScience, LifeScienceAdmin)
