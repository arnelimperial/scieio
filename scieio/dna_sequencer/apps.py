from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DnaSequencerConfig(AppConfig):
    name = 'scieio.dna_sequencer'
    verbose_name = _("DNA Sequencers")
