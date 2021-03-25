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
from AIAD.models import AIAD

# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "comment" + self.Post.title
class userComment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.User.firstName + self.User.lastName + 'comment'

class teamComment(models.Model):
    teamComment = models.ForeignKey(Team, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.Team.name + 'comment'

class projectComment(models.Model):
    projectComment = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.Project.name + 'comment'

class departmentComment(models.Model):
    departmentComment = models.ForeignKey(Department, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.Department.name + 'comment'

class commentAIAD(models.Model):
    aiadComment = models.ForeignKey(AIAD, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.AIAD.name + 'comment'
