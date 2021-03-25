from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django import forms
import datetime
from departments.models import Department
from projects.models import Project
from posts.models import Post
from teams.models import Team

# Create your models here.

class AIAD(models.Model):
    name = models.CharField(max_length=50, null=False)
    img = models.ImageField(default='', blank=True, upload_to='AIAD')
    link = models.URLField(
        max_length=2000,
        blank=True
    )
    mission = models.TextField()
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
        return self.name

class depAIAD(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    AIAD = models.ForeignKey(AIAD, on_delete=models.CASCADE)

    def __str__(self):
        return self.AIAD.name + self.Department.name

class postsAIAD(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    AIAD = models.ForeignKey(AIAD, on_delete=models.CASCADE)

    def __str__(self):
        return self.AIAD.name + self.Post.title


class teamAIAD(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    AIAD = models.ForeignKey(AIAD, on_delete=models.CASCADE)

    def __str__(self):
        return self.AIAD.name + self.Team.name

