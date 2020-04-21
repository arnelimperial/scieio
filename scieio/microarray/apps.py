from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MicroarrayConfig(AppConfig):
    name = 'scieio.microarray'
    verbose_name = _("Microarray Solutions")
