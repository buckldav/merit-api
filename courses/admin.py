from django.contrib import admin

from courses.models import Course, CourseTag

# Register your models here.
admin.site.register(Course)
admin.site.register(CourseTag)
