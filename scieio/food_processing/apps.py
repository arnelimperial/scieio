from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FoodProcessingConfig(AppConfig):
    name = 'scieio.food_processing'
    verbose_name = _("Food Processing Equipment")
