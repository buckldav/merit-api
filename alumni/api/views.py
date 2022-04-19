from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from alumni.models import Alum
from alumni.api.serializers import AlumSerializer


class AlumViewSet(ReadOnlyModelViewSet):
    serializer_class = AlumSerializer
    queryset = Alum.objects.all()
    permission_classes = [AllowAny]
