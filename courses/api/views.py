from rest_framework import viewsets, permissions
from .serializers import CourseSerializer
from courses.models import Course


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
