from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.core.exceptions import ValidationError
from scieio.analytical_instruments.models import Instrumentation
from scieio.manufacturers.models import Manufacturer
from scieio.sellers.models import Seller
from scieio.conditions.models import Condition
import random


class Spectrometry(models.Model):
    instrumentation = models.ForeignKey(
        Instrumentation,
        on_delete=models.CASCADE,
        related_name='instrumentations',
        related_query_name='instrumentation'
    )
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
        return reverse('spectrometry-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


def product_code_start():
    return random.randint(1, 99)


def product_code_end():
    return random.randint(1, 99)


def gas_count():
    obj_gas = GasMS.objects.latest('id')
    if obj_gas is None:
        return 1
    else:
        return obj_gas.id + 1


DEFAULT_GCMS = 1


class GasMS(models.Model):
    spectrometer = models.ForeignKey(
        Spectrometry,
        on_delete=models.CASCADE,
        related_name='gas_spectrometers',
        related_query_name='gas_spectrometer',
        default=DEFAULT_GCMS
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    description = models.TextField()
    product_code = models.CharField(
        unique=True,
        max_length=15,
        editable=False
    )
    model = models.CharField(max_length=255, unique=True)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    warranty = models.BooleanField(default=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    image = models.URLField()
    availability = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
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
        return reverse('gasMS-detail', kwargs=kwargs)

    def clean(self, *args, **kwargs):
        # code = self.cleaned_data['product_code']
        pc = GasMS.objects.filter(product_code=self.product_code)
        if pc:
            raise ValidationError('Product code already exist!')
        super(GasMS, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        self.product_code = "{}-{}{}{}".format(
            "GMS", product_code_start(), gas_count(), product_code_end()
        )
        self.full_clean()
        super().save(*args, **kwargs)


DEFAULT_LCMS = 1


def liquid_count():
    obj_liquid = LiquidMS.objects.latest('id')
    if obj_liquid is None:
        return 1
    else:
        return obj_liquid.id + 1


class LiquidMS(models.Model):
    spectrometer = models.ForeignKey(
        Spectrometry,
        on_delete=models.CASCADE,
        related_name='liquid_spectrometers',
        related_query_name='liquid_spectrometer',
        default=DEFAULT_LCMS
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    description = models.TextField()
    product_code = models.CharField(
        unique=True,
        max_length=15,
        editable=False
    )
    model = models.CharField(max_length=255, unique=True)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    warranty = models.BooleanField(default=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    image = models.URLField()
    availability = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
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
        return reverse('liquidMS-details', kwargs=kwargs)

    def clean(self, *args, **kwargs):
        # code = self.cleaned_data['product_code']
        pc = LiquidMS.objects.filter(product_code=self.product_code)
        if pc:
            raise ValidationError('Product code already exist!')
        super(LiquidMS, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        self.product_code = "{}-{}{}{}".format(
            "LMS", product_code_start(), liquid_count(), product_code_end()
        )
        self.full_clean()
        super().save(*args, **kwargs)
