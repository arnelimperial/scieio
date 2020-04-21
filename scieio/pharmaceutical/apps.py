from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PharmaceuticalConfig(AppConfig):
    name = 'scieio.pharmaceutical'
    verbose_name = _("Pharmaceutical Equipment")
