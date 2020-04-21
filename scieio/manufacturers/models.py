from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    website = models.URLField(max_length=100, blank=True)
    description = models.TextField(blank=False, default='')
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['id']
        unique_together = ('name', 'slug')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('manufacturer-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
