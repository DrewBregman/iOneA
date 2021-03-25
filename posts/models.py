from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django import forms
import datetime
from departments.models import Department
from projects.models import Project

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    img = models.ImageField(default='', blank=True, upload_to='post_image')
    link = models.URLField(
        max_length=2000,
        blank=True
    )

    body = models.TextField(default="", null=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    statusOptions = (
        ('Active', ('Active')),
        ('Archived', ('Archived')),
        ('Deleted', ('Deleted')),
    )

    status = models.CharField(
        max_length=50,
        choices=statusOptions,
        default='Active',
    )
    
    def __str__(self):
        return self.title


class uPosts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pType = (
        ('Tagged', ('Tagged')),
        ('Posted', ('Posted')),
        ('Liked', ('Liked')),
    )

    postType = models.CharField(
        max_length=50,
        choices=pType,
        default='Posted',
    )

    def __str__(self):
        return 'Post From' + self.user.firstName + (' ') + self.user.lastName

class depPosts(models.Model):
   
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pType = (
        ('Tagged', ('Tagged')),
        ('Posted', ('Posted')),
        ('Liked', ('Liked')),
    )

    postType = models.CharField(
        max_length=50,
        choices=pType,
        default='Posted',
    )

    def __str__(self):
        return 'Post From' + self.Department.name

class projPosts(models.Model):
   
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pType = (
        ('Tagged', ('Tagged')),
        ('Posted', ('Posted')),
        ('Liked', ('Liked')),
    )

    postType = models.CharField(
        max_length=50,
        choices=pType,
        default='Posted',
    )

    def __str__(self):
        return 'Post From' + self.Project.name