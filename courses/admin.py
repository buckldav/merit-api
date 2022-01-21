from django.contrib import admin

from courses.models import Course, CourseTag


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseTag)
