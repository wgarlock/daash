from daash.tenant.models import Tenant
from wagtail.contrib.modeladmin.helpers import PermissionHelper
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register


class TenantPermissionHelper(PermissionHelper):
    pass


class TenantModelAdmin(ModelAdmin):
    model = Tenant
    permission_helper_class = TenantPermissionHelper
    add_to_settings_menu = True


modeladmin_register(TenantModelAdmin)
