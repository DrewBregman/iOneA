
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django import forms
from departments.models import Department
from projects.models import Project

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    bPic = models.ImageField(default='defaultproban.jpg', upload_to='project_banner')
    logo = models.ImageField(default='defaultlogo.jpg', upload_to='project_logo')
    dep_choice1 = (
        ('Behavioral Sciences and Leadership', ('Behavioral Sciences and Leadership')),
        ('Chemistry and Life Science', ('Chemistry and Life Science')),
        ('Civil and Mechanical Engineering', ('Civil and Mechanical Engineering')),
        ('Electrical Engineering and Comptuer Science', ('Electrical Engineering and Comptuer Science')),
        ('English and Philosophy', ('English and Philosophy')),
        ('Foreign Languages', ('Foreign Languages')),
        ('Geography and Environmental Engineering', ('Geography and Environmental Engineering')),
        ('History', ('History')),
        ('Law', ('Law')),
        ('Mathematical Sciences', ('Mathematical Sciences')),
        ('Physics and Nuclear Engineering', ('Physics and Nuclear Engineering')),
        ('Social Sciences', ('Social Sciences')),
        ('Systems Engineering', ('Systems Engineering')),
        ('Independent', ('Independent')),
    )
    department = models.CharField(
        max_length=50,
        choices=dep_choice1,
        default='Independent',
    )
    description = models.CharField(max_length=50, null = True)
    purpose=models.TextField()
    tag_choice = (
        ('Data Analysis' , ('Data Analysis')),
        ('3D Printing' , ('3D Printing')),
        ('Robotics' , ('Robotics')),
        ('Coding' , ('Coding')),
        ('Aerodynamics' , ('Aerodynamics')),
    )

    projectTag = models.CharField(
        max_length=32,
        choices=tag_choice,
        default='Coding',
    )

    look = (
        ('motivated cadets with niche expertise.', ('Expert Cadets')),
        ('cadets who want to learn and help.', ('Any cadet who wants to help')),
        ('an engineering cadet.', ('Engineering Cadet')),
        ('a cadet with a scientific background.', ('Scientific background')),
        ('cadets with programming experience.', ('Coding Background')),
       
    )
    
    lookingFor = models.CharField(
        max_length=75,
        choices=look,
        default='an engineering cadet,',
    )

    recruit = (
        ('Yes', ('Yes')),
        ('No', ('No')),
    )

    recruiting = models.CharField(
        max_length=50,
        choices=recruit,
        default='Yes',
    )
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
    class Meta:
        verbose_name_plural= "teams"

    def __str__(self):
        return self.name

class userTeam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.User.firstName + self.User.lastName + self.Team.name

class departmentTeam(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.Department.name + self.Team.name

class projectTeam(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.Project.name + self.Team.name

