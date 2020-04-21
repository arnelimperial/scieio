from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AnalyticalInstrumentsConfig(AppConfig):
    name = 'scieio.analytical_instruments'
    verbose_name = _("Analytical Instruments")
