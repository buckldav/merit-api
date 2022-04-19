from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from alumni.api.views import AlumViewSet
from blog.api.views import CommentViewSet
from courses.api.views import CourseViewSet
from library.library.api.views import AuthorView, BookView, CheckoutView, StudentView, TeacherView

from library.users.api.views import UserViewSet
from projects.api.views import ProjectViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("alumni", AlumViewSet)
router.register("comments", CommentViewSet)
router.register("courses", CourseViewSet)
router.register("projects", ProjectViewSet)
router.register("library/users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
