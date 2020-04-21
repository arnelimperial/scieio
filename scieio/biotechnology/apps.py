from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BiotechnologyConfig(AppConfig):
    name = 'scieio.biotechnology'
    verbose_name = _("Biotechnology Equipment")
