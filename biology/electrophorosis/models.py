from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.core.exceptions import ValidationError
from biology.life_sciences.models import LifeScience
from generals.manufacturers.models import Manufacturer
from generals.sellers.models import Seller
from generals.conditions.models import Condition
import random


class ElectrophorosisCategory(models.Model):
    life_science = models.ForeignKey(LifeScience, on_delete=models.CASCADE)
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
        return reverse('electrophorosis-category-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

#
# class GCChroma(models.Model):
#     chromatography_category = models.ForeignKey(
#         ChromaCategory,
#         on_delete=models.CASCADE,
#         related_name='gcchromas',
#         related_query_name='gcchroma',
#     )
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, unique=True, editable=False)
#     created = models.DateTimeField(auto_now=False, auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True, auto_now_add=False)
#
#     class Meta:
#         ordering = ['id']
#         unique_together = ('name', 'slug')
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         kwargs = {
#             'pk': self.id,
#             'slug': self.slug
#         }
#         return reverse('gcChroma-detail', kwargs=kwargs)
#
#     def save(self, *args, **kwargs):
#         value = self.name
#         self.slug = slugify(value, allow_unicode=True)
#         super().save(*args, **kwargs)
#
#
# class LCChroma(models.Model):
#     chromatography_category = models.ForeignKey(
#         ChromaCategory,
#         on_delete=models.CASCADE,
#         related_name='lcchromas',
#         related_query_name='lcchroma',
#     )
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, unique=True, editable=False)
#     created = models.DateTimeField(auto_now=False, auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True, auto_now_add=False)
#
#     class Meta:
#         ordering = ['id']
#         unique_together = ('name', 'slug')
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         kwargs = {
#             'pk': self.id,
#             'slug': self.slug
#         }
#         return reverse('lcChroma-detail', kwargs=kwargs)
#
#     def save(self, *args, **kwargs):
#         value = self.name
#         self.slug = slugify(value, allow_unicode=True)
#         super().save(*args, **kwargs)
#
#
# # For GC Systems, Autosamplers and columns
#
# def product_code_start():
#     return random.randint(1, 99)
#
#
# def product_code_end():
#     return random.randint(1, 99)
#
#
# def gas_count():
#     obj_gas = GCSystem.objects.latest('id')
#     if obj_gas is None:
#         return 1
#     else:
#         return obj_gas.id + 1
#
#
# class GCSystem(models.Model):
#     gc_category = models.ForeignKey(
#         GCChroma,
#         on_delete=models.CASCADE,
#         related_name='gcsystems',
#         related_query_name='gcsystem'
#     )
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, unique=True, editable=False)
#     description = models.TextField()
#     product_code = models.CharField(
#         unique=True,
#         blank=False,
#         max_length=15,
#         editable=False
#     )
#     model = models.CharField(max_length=255, unique=True)
#     condition = models.ForeignKey(
#         Condition,
#         on_delete=models.CASCADE,
#         related_name='conditions',
#         related_query_name='condition'
#     )
#     warranty = models.BooleanField(default=True)
#     seller = models.ForeignKey(
#         Seller,
#         on_delete=models.CASCADE,
#         related_name='sellers',
#         related_query_name='seller'
#     )
#     manufacturer = models.ForeignKey(
#         Manufacturer,
#         on_delete=models.CASCADE,
#         related_name='manufacturers',
#         related_query_name='manufacturer'
#     )
#     image = models.URLField()
#     availability = models.BooleanField(default=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     created = models.DateTimeField(auto_now=False, auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True, auto_now_add=False)
#
#     class Meta:
#         ordering = ['id']
#         unique_together = ('name', 'slug')
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         kwargs = {
#             'pk': self.id,
#             'slug': self.slug
#         }
#         return reverse('gcSystem-detail', kwargs=kwargs)
#
#     def clean(self, *args, **kwargs):
#         # code = self.cleaned_data['product_code']
#         pc = GCSystem.objects.filter(product_code=self.product_code)
#         if pc:
#             raise ValidationError('Product code already exist!')
#         super(GCSystem, self).clean(*args, **kwargs)
#
#     def save(self, *args, **kwargs):
#         value = self.name
#         self.slug = slugify(value, allow_unicode=True)
#         self.product_code = "{}-{}{}{}".format(
#             "GC", product_code_start(), gas_count(), product_code_end()
#         )
#         self.full_clean()
#         super().save(*args, **kwargs)
#
#
# def liquid_count():
#     obj_liquid = LiquidMS.objects.latest('id')
#     if obj_liquid is None:
#         return 1
#     else:
#         return obj_liquid.id + 1
#
#
# class LC(models.Model):
#     lc_category = models.ForeignKey(
#         LCChroma,
#         on_delete=models.CASCADE,
#         related_name='lcs',
#         related_query_name='lc'
#     )
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, unique=True, editable=False)
#     description = models.TextField()
#     product_code = models.CharField(
#         unique=True,
#         blank=False,
#         max_length=15,
#         editable=False
#     )
#     model = models.CharField(max_length=255, unique=True)
#     condition = models.ForeignKey(
#         Condition,
#         on_delete=models.CASCADE,
#         related_name='lcconditions',
#         related_query_name='lccondition'
#     )
#     warranty = models.BooleanField(default=True)
#     seller = models.ForeignKey(
#         Seller,
#         on_delete=models.CASCADE,
#         related_name='lcsellers',
#         related_query_name='lcseller'
#     )
#     manufacturer = models.ForeignKey(
#         Manufacturer,
#         on_delete=models.CASCADE,
#         related_name='lcmanufacturers',
#         related_query_name='lcmanufacturer'
#     )
#     image = models.URLField()
#     availability = models.BooleanField(default=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     created = models.DateTimeField(auto_now=False, auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True, auto_now_add=False)
#
#     class Meta:
#         ordering = ['id']
#         unique_together = ('name', 'slug')
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         kwargs = {
#             'pk': self.id,
#             'slug': self.slug
#         }
#         return reverse('lc-detail', kwargs=kwargs)
#
#     def clean(self, *args, **kwargs):
#         # code = self.cleaned_data['product_code']
#         pc = GCSystem.objects.filter(product_code=self.product_code)
#         if pc:
#             raise ValidationError('Product code already exist!')
#         super(LC, self).clean(*args, **kwargs)
#
#     def save(self, *args, **kwargs):
#         value = self.name
#         self.product_code = "{}-{}{}{}".format(
#             "LC", product_code_start(), liquid_count(), product_code_end()
#         )
#         self.slug = slugify(value, allow_unicode=True)
#         self.full_clean()
#         super().save(*args, **kwargs)
