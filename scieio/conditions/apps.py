from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ConditionsConfig(AppConfig):
    name = 'scieio.conditions'
    verbose_name = _("Product Conditions")
