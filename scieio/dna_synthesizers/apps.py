from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DnaSynthesizersConfig(AppConfig):
    name = 'scieio.dna_synthesizers'
    verbose_name = _("DNA Synthesizers")
