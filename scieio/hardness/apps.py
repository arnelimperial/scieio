from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HardnessConfig(AppConfig):
    name = 'scieio.hardness'
    verbose_name = _("Hardness Testers")
