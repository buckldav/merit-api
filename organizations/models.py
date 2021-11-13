from django.db import models
from rest_framework_api_key.models import AbstractAPIKey, BaseAPIKeyManager


class Organization(models.Model):
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=True)


class OrganizationAPIKey(AbstractAPIKey):
    class Meta(AbstractAPIKey.Meta):
        verbose_name = "Organization API Key"
        verbose_name_plural = "Organization API Keys"

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="api_keys",
    )


class BlogAPIKey(OrganizationAPIKey):
    class Meta(AbstractAPIKey.Meta):
        verbose_name = "Blog API Key"
        verbose_name_plural = "Blog API Keys"

    email = models.EmailField(unique=True)


class OrganizationAPIKeyManager(BaseAPIKeyManager):
    def get_usable_keys(self):
        return super().get_usable_keys().filter(organization__active=True)
