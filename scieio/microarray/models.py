from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.core.exceptions import ValidationError
from scieio.life_sciences.models import LifeScience
from scieio.manufacturers.models import Manufacturer
from scieio.sellers.models import Seller
from scieio.conditions.models import Condition
import random


def product_code_start():
    return random.randint(1, 99)


def product_code_end():
    return random.randint(1, 99)


def microarray_count():
    obj = MicroArrayScanner.objects.all().count()
    if obj == 0:
        return 1
    else:
        return obj + 1


class MicroArrayScanner(models.Model):
    life_science = models.ForeignKey(LifeScience, on_delete=models.CASCADE)
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
        return reverse('microArrayScanner-detail', kwargs=kwargs)

    def clean(self, *args, **kwargs):
        # code = self.cleaned_data['product_code']
        pc = MicroArrayScanner.objects.filter(product_code=self.product_code)
        if pc:
            raise ValidationError('Product code already exist!')
        super(MicroArrayScanner, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        self.product_code = "{}-{}{}{}".format(
            "MAS", product_code_start(), microarray_count(), product_code_end()
        )
        self.full_clean()
        super().save(*args, **kwargs)
