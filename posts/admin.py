from django.contrib import admin
from .models import Post, uPosts, depPosts, projPosts
# Register your models here.
admin.site.register(Post)
admin.site.register(uPosts)
admin.site.register(depPosts)
admin.site.register(projPosts)