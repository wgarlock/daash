from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FrontConfig(AppConfig):
    name = 'daash.front'
    label = 'daashfront'
    verbose_name = _("Wes Garlock Front")
