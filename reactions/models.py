from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django import forms
import datetime
from departments.models import Department
from projects.models import Project
from posts.models import Post
from directMessage.models import Message
from comments.models import Comment
from teams.models import Team

# Create your models here.

class Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, blank=True)
    reaction = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Reaction.reaction + self.Post.name

class userReaction(models.Model):
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.User.name + self.Reaction.reaction

class projectReaction(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)

    def __str__(self):
        return self.Project.name + self.Reaction.reaction
class departmentReaction(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)

    def __str__(self):
        return self.Department.name + self.Reaction.reaction


class teamReaction(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)

    def __str__(self):
        return self.Team.name + self.Reaction.reaction
