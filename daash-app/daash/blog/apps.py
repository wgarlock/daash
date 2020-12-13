from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogConfig(AppConfig):
    name = 'daash.blog'
    label = 'daashblog'
    verbose_name = _("Wes Garlock Blog")
