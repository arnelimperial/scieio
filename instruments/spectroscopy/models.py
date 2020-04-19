from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.core.exceptions import ValidationError
from instruments.analytical_instruments.models import Instrumentation
from generals.manufacturers.models import Manufacturer
from generals.sellers.models import Seller
from generals.conditions.models import Condition
import random


class Spectroscopy(models.Model):
    instrumentation = models.ForeignKey(Instrumentation, on_delete=models.CASCADE)
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
        return reverse('spectroscopy-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


def product_code_start():
    return random.randint(1, 99)


def product_code_end():
    return random.randint(1, 99)


def aa_count():
    obj_gas = AtomicAbsorption.objects.all().count()
    if obj_gas == 0:
        return 1
    else:
        return obj_gas + 1


class AtomicAbsorption(models.Model):
    spectroscopy_category = models.ForeignKey(
        Spectroscopy,
        on_delete=models.CASCADE,
        related_name='atomics',
        related_query_name='atomic'
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    description = models.TextField()
    product_code = models.CharField(
        unique=True,
        blank=False,
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
        return reverse('gcSystem-detail', kwargs=kwargs)

    def clean(self, *args, **kwargs):
        # code = self.cleaned_data['product_code']
        pc = AtomicAbsorption.objects.filter(product_code=self.product_code)
        if pc:
            raise ValidationError('Product code already exist!')
        super(AtomicAbsorption, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        self.product_code = "{}-{}{}{}".format(
            "AA", product_code_start(), aa_count(), product_code_end()
        )
        self.full_clean()
        super().save(*args, **kwargs)


def spectrophotometer_count():
    obj_gas = Spectrophotometer.objects.latest('id')
    if obj_gas.id == 0:
        return 1
    else:
        return obj_gas.id + 1


class Spectrophotometer(models.Model):
    spectroscopy_category = models.ForeignKey(Spectroscopy, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    description = models.TextField()
    product_code = models.CharField(
        unique=True,
        blank=False,
        max_length=10,
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
        return reverse('lc-detail', kwargs=kwargs)

    def clean(self, *args, **kwargs):
        # code = self.cleaned_data['product_code']
        pc = Spectrophotometer.objects.filter(product_code=self.product_code)
        if pc:
            raise ValidationError('Product code already exist!')
        super(Spectrophotometer, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.product_code = "{}-{}{}{}".format(
            "SP", product_code_start(), spectrophotometer_count(), product_code_end()
        )
        self.slug = slugify(value, allow_unicode=True)
        self.full_clean()
        super().save(*args, **kwargs)


def icp_count():
    obj_gas = ICP.objects.all().count()
    if obj_gas == 0:
        return 1
    else:
        return obj_gas + 1


class ICP(models.Model):
    spectroscopy_category = models.ForeignKey(
        Spectroscopy,
        on_delete=models.CASCADE,
        related_name='icps',
        related_query_name='icp'
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    description = models.TextField()
    product_code = models.CharField(
        unique=True,
        blank=False,
        max_length=15,
        editable=False
    )
    model = models.CharField(max_length=255, unique=True)
    condition = models.ForeignKey(Condition,on_delete=models.CASCADE)
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
        return reverse('icp-detail', kwargs=kwargs)

    def clean(self, *args, **kwargs):
        # code = self.cleaned_data['product_code']
        pc = ICP.objects.filter(product_code=self.product_code)
        if pc:
            raise ValidationError('Product code already exist!')
        super(ICP, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        self.product_code = "{}-{}{}{}".format(
            "ICP", product_code_start(), icp_count(), product_code_end()
        )
        self.full_clean()
        super().save(*args, **kwargs)


def ftir_count():
    obj_liquid = FTIR.objects.all().count()
    if obj_liquid == 0:
        return 1
    else:
        return obj_liquid + 1


class FTIR(models.Model):
    spectroscopy_category = models.ForeignKey(
        Spectroscopy,
        on_delete=models.CASCADE,
        related_name='ftirs',
        related_query_name='ftir'
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    description = models.TextField()
    product_code = models.CharField(
        unique=True,
        blank=False,
        max_length=10,
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
        return reverse('lc-detail', kwargs=kwargs)

    def clean(self, *args, **kwargs):
        # code = self.cleaned_data['product_code']
        pc = FTIR.objects.filter(product_code=self.product_code)
        if pc:
            raise ValidationError('Product code already exist!')
        super(FTIR, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.product_code = "{}-{}{}{}".format(
            "FT", product_code_start(), ftir_count(), product_code_end()
        )
        self.slug = slugify(value, allow_unicode=True)
        self.full_clean()
        super().save(*args, **kwargs)
