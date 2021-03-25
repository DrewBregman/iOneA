from django.contrib import admin
from .models import Reaction, userReaction, departmentReaction, teamReaction, projectReaction
# Register your models here.
admin.site.register(Reaction)
admin.site.register(userReaction)
admin.site.register(departmentReaction)
admin.site.register(teamReaction)
admin.site.register(projectReaction)