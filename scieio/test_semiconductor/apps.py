from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TestSemiconductorConfig(AppConfig):
    name = 'scieio.test_semiconductor'
    verbose_name = _("Testers and Semiconductor Categories")
