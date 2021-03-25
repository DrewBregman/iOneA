from django.contrib import admin
from .models import ToDoList, Item, User

# Register your models here.

admin.site.register(ToDoList)
admin.site.register(Item)


