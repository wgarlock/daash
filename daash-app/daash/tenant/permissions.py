from daash.tenant.models import Tenant
from wagtail.core.permission_policies import ModelPermissionPolicy

tenant_permission_policy = ModelPermissionPolicy(Tenant)
