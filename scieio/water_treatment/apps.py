from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WaterTreatmentConfig(AppConfig):
    name = 'scieio.water_treatment'
    verbose_name = _("Water Treatment Equipment")
