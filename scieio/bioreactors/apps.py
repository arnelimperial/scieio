from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BioreactorsConfig(AppConfig):
    name = "scieio.bioreactors"
    verbose_name = _("Fermenters and Bioreactors")
