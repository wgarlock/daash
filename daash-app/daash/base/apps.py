from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BaseConfig(AppConfig):
    name = 'daash.base'
    label = 'daashbase'
    verbose_name = _("Wes Garlock Base")

    def ready(self):
        from daash.base.conf import BaseAppConf  # noqa
