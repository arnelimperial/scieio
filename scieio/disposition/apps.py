from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DispositionConfig(AppConfig):
    name = 'scieio.disposition'
    verbose_name = _("Disposition")
