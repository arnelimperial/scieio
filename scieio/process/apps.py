from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProcessConfig(AppConfig):
    name = 'scieio.process'
    verbose_name = _("Process Equipment")
