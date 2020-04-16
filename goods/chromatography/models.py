from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from goods.categories.models import Category


class ChromaCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
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
        return reverse('chromaCategory-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class GCChroma(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
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
        return reverse('gcChroma-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class LCChroma(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
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
        return reverse('lcChroma-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)





    # class Product(models.Model):
    # product_category =
    # instrument_category =
    # chromatography_category =
    # name = models.CharField(max_length=255)
    # slug = models.SlugField(max_length=255, unique=True, editable=False)
    # description =
    # details_id =
    # model_number =
    # condition =
    # warranty =
    # seller_name =
    # seller_location =
    # manufacturer =
    # price =
    # created = models.DateTimeField(auto_now=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    #
    # class Meta:
    #     ordering = ['id']
    #     unique_together = ('name', 'slug')
    #
    # def __str__(self):
    #     return self.name
    #
    # def get_absolute_url(self):
    #     kwargs = {
    #         'pk': self.id,
    #         'slug': self.slug
    #     }
    #     return reverse('chromaCategory-detail', kwargs=kwargs)

    # def save(self, *args, **kwargs):
    #     value = self.name
    #     self.slug = slugify(value, allow_unicode=True)
    #     super().save(*args, **kwargs)

