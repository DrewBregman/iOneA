from django.db import models
import datetime
from django import forms
from projects.models import Project
from django.contrib.auth.models import User
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=30)
    mission = models.CharField(max_length = 100)
    departmentHead = models.OneToOneField(User, on_delete=models.CASCADE, related_name="departmentHead")
    deputyHead = models.OneToOneField(User, on_delete=models.CASCADE, related_name="deputyHead")
    dac = models.OneToOneField(User, on_delete=models.CASCADE, related_name="DAC")
    depBanner = models.ImageField(default='', blank=True, upload_to='department_banner')
    depLogo = models.ImageField(default='', blank=True, upload_to='department_logo')
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

class uDepartment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username + ',' + self.department.name

class projDepartment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.project.name + ',' + self.department.name


