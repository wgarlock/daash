from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

from . import checks  # NOQA
from .signal_handlers import register_signal_handlers


class TenantConfig(AppConfig):
    name = 'daash.tenant'
    label = 'daashtenant'
    verbose_name = _("Wes Garlock Tenant")

    def ready(self):
        register_signal_handlers(self)
