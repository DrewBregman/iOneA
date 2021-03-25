from django.contrib import admin
from .models import Comment, userComment, teamComment, projectComment, departmentComment, commentAIAD
# Register your models here.
admin.site.register(Comment)
admin.site.register(userComment)
admin.site.register(teamComment)
admin.site.register(projectComment)
admin.site.register(departmentComment)
admin.site.register(commentAIAD)