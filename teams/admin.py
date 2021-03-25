from django.contrib import admin
from .models import Team, userTeam, projectTeam, departmentTeam
# Register your models here.
admin.site.register(Team)
admin.site.register(userTeam)
admin.site.register(projectTeam)
admin.site.register(departmentTeam)