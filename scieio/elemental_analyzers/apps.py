from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ElementalAnalyzersConfig(AppConfig):
    name = 'scieio.elemental_analyzers'
    verbose_name = _("Elemental Analyzers")
