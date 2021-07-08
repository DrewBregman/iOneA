from django.contrib import admin
from .models import ToDoList, Item, User, Department,uDeparment,uProjects,projDepartment

# Register your models here.

admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(Department)
admin.site.register(uDeparment)
admin.site.register(uProjects)
admin.site.register(projDepartment)
