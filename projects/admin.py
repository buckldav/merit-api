from django.contrib import admin
from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'project_type')
    list_filter = ('project_type', )


admin.site.register(Project, ProjectAdmin)
