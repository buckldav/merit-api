from django.contrib import admin
from organizations.models import Organization, OrganizationAPIKey, BlogAPIKey
from rest_framework_api_key.admin import APIKeyModelAdmin


@admin.register(OrganizationAPIKey)
class OrganizationAPIKeyModelAdmin(APIKeyModelAdmin):
    pass


@admin.register(BlogAPIKey)
class BlogAPIKeyModelAdmin(APIKeyModelAdmin):
    pass


admin.site.register(Organization)
