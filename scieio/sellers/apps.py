from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SellersConfig(AppConfig):
    name = 'scieio.sellers'
    verbose_name = _("Sellers")
