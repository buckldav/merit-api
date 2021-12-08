from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from projects.api.serializers import ProjectSerializer
from projects.models import Project


class ProjectViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [AllowAny]
