from daash.tenant.constants import SITE_OWNER_GROUP_NAME
from daash.tenant.models import Tenant
from daash.tenant.utils import establish_connection
from fixtures.base import tenants  # noqa
from wagtail.core.models import Group


def test_tenants(db) -> None:
    for tenant in Tenant.objects.all():
        assert establish_connection(tenant.domain) is not None
        assert Group.objects.db_manager(
            using=tenant.domain.lower()
        ).filter(name=SITE_OWNER_GROUP_NAME).first() is not None
