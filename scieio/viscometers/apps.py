from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ViscometersConfig(AppConfig):
    name = 'scieio.viscometers'
    verbose_name = _("Viscometers and Rheometers")
