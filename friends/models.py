from django.db import models
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
class Friend(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requester")
    accepter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accepter")
    message = models.CharField(max_length=200, default='', blank=True)
    url = models.URLField(null='', blank='', default='')
    ifViewed = models.BooleanField(null=False, default=False)
    ifAccepted = models.BooleanField(null=False, default=False)
    def __str__(self):
        return self.message