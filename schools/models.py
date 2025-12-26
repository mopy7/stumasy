from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class School(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)

    # Default true, schema will be automatically created with the tenant
    auto_create_schema = True

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    pass
