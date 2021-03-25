from django.contrib import admin

# Register your models here.
from .models import Project, uProjects

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "department", "description",)
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(uProjects)