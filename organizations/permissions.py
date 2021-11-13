from rest_framework_api_key.permissions import BaseHasAPIKey
from rest_framework import permissions
from .models import OrganizationAPIKey, BlogAPIKey


class HasOrganizationAPIKey(BaseHasAPIKey):
    model = OrganizationAPIKey


class HasBlogAPIKey(BaseHasAPIKey):
    model = BlogAPIKey


class IsAdminOrHasBlogAPIKey(permissions.BasePermission):
    message = 'None of permissions requirements fulfilled.'

    def has_permission(self, request, view):
        return request.user.is_superuser or HasBlogAPIKey().has_permission(request, view)
