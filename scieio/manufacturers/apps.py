from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ManufacturersConfig(AppConfig):
    name = 'scieio.manufacturers'
    verbose_name = _("Manufacturers")
