from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from generals.manufacturers.models import Manufacturer
from generals.categories.models import Category


class Seller(models.Model):
    service_line = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='services',
        related_query_name='service'
    )
    client_manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='client_manufacturers',
        related_query_name='client_manufacturer'
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    location = models.CharField(max_length=100)
    website = models.URLField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    shipping_policy = models.TextField(default='No Shipping Policy Listed')
    return_policy = models.TextField(default='No Return Policy Listed')
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
        return reverse('seller-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
