from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SpectroscopyConfig(AppConfig):
    name = 'scieio.spectroscopy'
    verbose_name = _("Spectroscopy")
