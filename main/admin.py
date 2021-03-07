from django.contrib import admin
from .models import ToDoList, Item, User, userID, uBio, Department

# Register your models here.

admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(User)
admin.site.register(userID)
admin.site.register(uBio)
admin.site.register(Department)
